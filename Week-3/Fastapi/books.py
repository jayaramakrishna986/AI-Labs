from fastapi import Body,FastAPI

app=FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def first_app():
    return BOOKS

# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param):
#     return{"Dynamic parameter :" ,dynamic_param}


@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book
        

@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return=[]

    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)

        return books_to_return
    

@app.get("books/{book_author}")

async def read_author_category_by_query(bookauthor:str,category:str):
    book_to_return =[]
    for book in BOOKS:
        if book.get('author').casefold()==bookauthor.casefold() and \
                book.get('category').casefold()==category.casefold():
            book_to_return.append(book)
        return book_to_return
    

@app.post("/books/create_book")
def create_book(newbook=Body()):
    BOOKS.append(newbook)


@app.put("/books/updated_book")
def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
            BOOKS[i]=updated_book


@app.delete("/Books/delete_book/{book_title}")
def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
            BOOKS.pop(1)
            break


@app.get("/books/author/{author_name}")
async def searchby_author(author_name:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold()==author_name.casefold():
            books_to_return.append(book)
    return books_to_return

