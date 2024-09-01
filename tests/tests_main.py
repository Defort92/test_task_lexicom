from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_write_data():
    response = client.post("/write_data", json={"phone": "89090000000", "address": "Test Address"})
    assert response.status_code == 201
    assert response.json() == {"message": "Data successfully written/updated."}


def test_check_data_existing():
    client.post("/write_data", json={"phone": "89090000000", "address": "Test Address"})
    response = client.get("/check_data", params={"phone": "89090000000"})
    assert response.status_code == 200
    assert response.json() == {"phone": "89090000000", "address": "Test Address"}


def test_check_data_non_existing():
    response = client.get("/check_data", params={"phone": "1234567890"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Address not found for the given phone number."}
