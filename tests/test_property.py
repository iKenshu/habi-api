from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_property_status_code():
    response = client.get("/property/all/")
    assert response.status_code == 200


def test_property_params_status_code():
    response = client.get("/property/")
    assert response.status_code == 200
