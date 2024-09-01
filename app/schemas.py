from pydantic import BaseModel, Field, constr


class WriteDataRequest(BaseModel):
    phone: constr(regex=r'^\d{10,15}$') = Field(..., example="89090000000")
    address: str = Field(..., example="123 Main Street, City, Country")


class CheckDataResponse(BaseModel):
    phone: constr(regex=r'^\d{10,15}$') = Field(..., example="89090000000")
    address: str = Field(..., example="123 Main Street, City, Country")
