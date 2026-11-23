from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from src.books.book_data import books
from src.books.schemas import  Book,Book_update_model
from typing import List
app= FastAPI()



    
