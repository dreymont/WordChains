from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200

def test_chain_cat_to_dog():
    response = client.get("/wordchains/cat/dog")

    assert response.status_code == 200
    data = response.json()

    assert data["chain"][0] == "cat"
    assert data["chain"][-1] == "dog"

def test_different_length_words():
    response = client.get("/wordchains/cat/gold")

    assert response.status_code == 400

def test_word_not_found():
    response = client.get("/wordchains/xyz/dog")

    assert response.status_code == 404

def test_different_length_words_message():
    response = client.get("/wordchains/cat/gold")
    data = response.json()
    assert data["detail"] == "Words must be the same length"