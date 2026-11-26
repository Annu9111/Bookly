from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel,Book_update_model
from sqlmodel import select,dec
from .models import Book

class BookService:
    async def get_all_books(self,session:AsyncSession):
        statement = select(Book).order_by(dec(Book.created_at))
        result = await session.exec(statement)
        return result.all()
    
    async def get_a_book(self,book_uid:str,session:AsyncSession):
        statement = select(Book).where(Book.uid==book_uid)
        result = await session.exec(statement)
        return result.first()
    
    async def create_book(self,book_data:BookCreateModel,session:AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Book(
            **book_data_dict
        )
        session.add(new_book)
        await session.commit()
        return new_book
    
    async def update_book(self,book_uuid:str,update_data:Book_update_model,session:AsyncSession):
        book_to_update = self.get_a_book(book_uuid,session)
        
        if book_to_update is not None:
            
            update_data_dict = update_data.model_dump()
        
            for k , v in update_data_dict.items():
                setattr(book_to_update,k,v)
            await session.commit()
            return book_to_update
        
        else:
            return None
    
    async def delete_a_book(self,book_uuid:str,session:AsyncSession):
        pass
    
        