from fastapi.testclient import TestClient

from .. import books_controller

client = TestClient(books_controller.router)

def test_create_book():
  body = {
    "id": 0,
    "titulo": "Código Limpo",
    "foto": None,
    "editora": "Alta Books Editora",
    "autores": ["Robert C. Martin"]
  }
  response = client.post("/obras", json=body)
  assert response.status_code == 200
  assert response.json() == body

def test_get_book():
  body = {
    "id": 0,
    "titulo": "Código Limpo",
    "foto": None,
    "editora": "Alta Books Editora",
    "autores": ["Robert C. Martin"]
  }
  client.post("/obras", json=body)
  response = client.get("/obras")
  assert response.status_code == 200
  assert response.json() == { '0': body }