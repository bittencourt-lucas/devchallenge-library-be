from fastapi import FastAPI
from core.modules.books.controllers import books_controller

app = FastAPI()

app.include_router(books_controller.router)