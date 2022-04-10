from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
  id: int
  titulo: str
  editora: str
  foto: str | None = None
  autores: list

app = FastAPI()

fake_db = {}

@app.post("/obras", response_model=Book)
async def create_book(book: Book):
  fake_db[book.id] = book
  return book

@app.get("/obras", response_model=Book)
async def read_books():
  return fake_db

@app.put("/obras/{id}", response_model=Book)
async def update_book(id: str):
  return { "message": id }

@app.delete("/obras/{id}")
async def delete_book(id: str):
  return { "message": id + " was deleted successfully!" }