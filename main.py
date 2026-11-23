from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import List
app= FastAPI()

books=[
    {
    "id": 1,
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "publisher": "No Starch Press",
    "published_date": "2023-01-01",
    "page_count": 560,
    "language": "English",
},
{
    "id": 2,
    "title": "Fluent Python",
    "author": "Luciano Ramalho",
    "publisher": "O'Reilly Media",
    "published_date": "2022-03-15",
    "page_count": 1014,
    "language": "English",
},
{
    "id": 3,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "publisher": "Prentice Hall",
    "published_date": "2008-08-01",
    "page_count": 464,
    "language": "English",
},
{
    "id": 4,
    "title": "The Pragmatic Programmer",
    "author": "David Thomas",
    "publisher": "Addison-Wesley",
    "published_date": "2019-09-13",
    "page_count": 352,
    "language": "English",
},
{
    "id": 5,
    "title": "Automate the Boring Stuff with Python",
    "author": "Al Sweigart",
    "publisher": "No Starch Press",
    "published_date": "2019-11-12",
    "page_count": 592,
    "language": "English",
},
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count:int
    language: str
    
class Book_update_model(BaseModel):
    title: str
    author: str
    publisher: str 
    page_count:int
    language: str
    

@app.get("/Books",response_model=List[Book])
async def get_all_book(): 
    return books

@app.post("/Books",status_code=status.HTTP_201_CREATED)
async def create_a_book(Book_data:Book)->dict:
    new_book = Book_data.model_dump()
    books.append(new_book)
    return new_book
    

@app.get("/Books/{Book_id}")
async def get_a_book(Book_id:int):
    for book in books:
        if book["id"]==Book_id:
            return book
    raise HTTPException(status_code=404,detail="id not found")


@app.patch("/Books/{Book_id}")
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


@app.delete("/Book/{Book_id}")
async def delete_book(Book_id:int):
    for book in books:
        if book["id"]==Book_id:
            books.remove(book)
    raise HTTPException(status_code=404,detail="id not found")

