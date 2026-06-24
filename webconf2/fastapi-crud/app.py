import aiosqlite
from aiosqlite import Connection

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from models.books import Books

app = FastAPI()

async def get_conn():
    conn = await aiosqlite.connect("db/app.db")
    try:
        yield conn
    finally:
        await conn.close()

class BookCreate(BaseModel):
    title: str
    author: str

@app.post("/books")
async def add_book(book: BookCreate, conn: Connection = Depends(get_conn)):
    model = Books(conn)
    await model.add_book(book.title, book.author)
    return { "message": "Book added" }

@app.get("/books")
async def get_books(title: str = "", conn: Connection = Depends(get_conn)):
    model = Books(conn)
    return await model.search(title)


