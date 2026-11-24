
from sqlmodel import SQLModel, Field
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
import uuid


class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )

    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

    created_at: datetime = Field(
        default_factory=datetime.now
    )

    updated_at: datetime = Field(
        default_factory=datetime.now
    )

    def __repr__(self):
        return f"<Book {self.title}>"
