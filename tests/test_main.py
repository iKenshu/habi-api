from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_status_code_and_message():
    response = client.get("/")
    message_expected = {
        "Message": "Welcome, you have different options to use this API. /docs for documentation"
    }
    assert response.status_code == 200
    assert response.json() == message_expected
