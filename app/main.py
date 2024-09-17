from fastapi import FastAPI, Depends, HTTPException, status
from app.dependencies import get_redis_client
from app.schemas import WriteDataRequest, CheckDataResponse
from app.crud import write_data, get_address
from app.logging_config import setup_logging
import logging


setup_logging()

logger = logging.getLogger("app_logger")
error_logger = logging.getLogger("error_logger")

app = FastAPI(
    title="Phone Address Service",
    description="API для записи и получения адресов по номерам телефонов",
    version="1.0.0"
)


@app.post("/write_data", status_code=status.HTTP_201_CREATED)
async def write_data_endpoint(request: WriteDataRequest, client: aioredis.Redis = Depends(get_redis_client)):
    try:
        await write_data(client, request.phone, request.address)
        logger.info(f"Data written/updated for phone: {request.phone}")
        return {"message": "Data successfully written/updated."}
    except Exception as e:
        error_logger.error(f"Error writing data for phone: {request.phone}, error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/check_data", response_model=CheckDataResponse)
async def check_data_endpoint(phone: str, client: aioredis.Redis = Depends(get_redis_client)):
    try:
        address = await get_address(client, phone)
        if address is None:
            error_logger.warning(f"Address not found for phone: {phone}")
            raise HTTPException(status_code=404, detail="Address not found for the given phone number.")
        logger.info(f"Address retrieved for phone: {phone}")
        return CheckDataResponse(phone=phone, address=address)
    except Exception as e:
        error_logger.error(f"Error retrieving data for phone: {phone}, error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
