import httpx

def test_health(server):
    response = httpx.get("http://localhost:8000/health")
    assert response.status_code == 200

def test_chain_cat_to_dog(server):
    response = httpx.get("http://localhost:8000/wordchains/cat/dog")
    assert response.status_code == 200

def test_word_not_found(server):
    response = httpx.get("http://localhost:8000/wordchains/xyz/dog")
    assert response.status_code == 404