from fastapi import APIRouter
from ..models.book import Book

router = APIRouter()

fake_db = {}

@router.post("/obras", response_model=Book)
async def create_book(book: Book):
  fake_db[book.id] = book
  return book

@router.get("/obras", response_model=dict)
async def read_books():
  return fake_db

@router.put("/obras/{id}", response_model=Book)
async def update_book(id: str):
  return { "message": id }

@router.delete("/obras/{id}")
async def delete_book(id: str):
  return { "message": id + " was deleted successfully!" }