from pydantic import BaseModel

class Book(BaseModel):
  id: int
  titulo: str
  editora: str
  foto: str | None = None
  autores: list
