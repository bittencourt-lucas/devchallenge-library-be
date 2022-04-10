from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_book():
  body = {
    "id": 0,
    "titulo": "Código Limpo",
    "foto": None,
    "editora": "Alta Books Editora",
    "autores": ["Robert C. Martin"]
  }
  response = client.post(
    "/obras",
    json=body
  )
  assert response.status_code == 200
  assert response.json() == body