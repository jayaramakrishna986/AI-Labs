from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,Field
from typing import Optional
app=FastAPI()




class Book:
    id :int 
    title :str
    author : str
    description : str
    rating :int
    published_date:int


    def __init__(self,id,title,author,description,rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)


# @app.post("/book/add_book")
# def add_book(add_book:Book):
#     BOOKS.append(add_book)

# @app.get("/books/{book_id}")
# async def read_book(book_id:int =Path(gt=0)):
#     for book in BOOKS:
#         if book.id ==book_id:
#             return book
#     raise HTTPException(status_code=404,detail="Item is not found")

# @app.get("/books/")
# async def searchbyrating(brating:int=Query(gt=0,ls=6)):
#     books_to_return =[]
#     for i in BOOKS:
#         if i.rating==brating:
#             books_to_return.append(i)
#     return books_to_return



# @app.put("/books/update_book")
# async def update_book(new_book:BookRequest):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].id==new_book.id:
#             BOOKS[i]=new_book
        
@app.get("/books/{date_published}")
async def get_by_date(date_published:int ):
    return_books=[]
    for book in BOOKS:
        if book.published_date==date_published:
            return_books.append(book)
    return return_books