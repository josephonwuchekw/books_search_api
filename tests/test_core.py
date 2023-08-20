from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_root_returns_json():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()


# def test_get_books_valid_query():
#     response = client.get("/api/v1/books/?q=mohicans")
#     assert response.status_code == 200


# def test_get_books_empty_query():
#     response = client.get("/api/v1/books/?q=")
#     assert response.status_code == 400
