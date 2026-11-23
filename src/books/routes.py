from fastapi import APIRouter,status,HTTPException
from pydantic import BaseModel
from src.books.book_data import books
from src.books.schemas import  Book,Book_update_model
from typing import List 

book_router = APIRouter()

@book_router.get("/",response_model=List[Book])
async def get_all_book(): 
    return books

@book_router.post("/",status_code=status.HTTP_201_CREATED)
async def create_a_book(Book_data:Book)->dict:
    new_book = Book_data.model_dump()
    books.append(new_book)
    return new_book
    

@book_router.get("/{Book_id}")
async def get_a_book(Book_id:int):
    for book in books:
        if book["id"]==Book_id:
            return book
    raise HTTPException(status_code=404,detail="id not found")


@book_router.patch("/{Book_id}")
async def update_book(Book_id:int,book_update_data :Book_update_model):
    for book in books:
        if book["id"]==Book_id:
            book['title'] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return book
    raise HTTPException(status_code=404,detail="Book id not found")


@book_router.delete("/{Book_id}")
async def delete_book(Book_id:int):
    for book in books:
        if book["id"]==Book_id:
            books.remove(book)
    raise HTTPException(status_code=404,detail="id not found")



