import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the SnapGarden API!"}

def test_analyze_image():
    with open("/home/baran/dataset_hub/dataset_converted/Alocasia (Elephant Ear)/1.jpg", "rb") as image_file:
        response = client.post(
            "/analyze",
            files={"file": image_file},
            data={"question": "Is this a plant?"}
        )
    assert response.status_code == 200
    assert "answer" in response.json()
    print(response.json())