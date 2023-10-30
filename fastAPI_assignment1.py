from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/get_books/{author}")
async def get_books_by_author_path(author : str):
    books_list = []
    for books in BOOKS:
        if books.get('author').casefold() == author.casefold():
            books_list.append(books)
    return books_list


@app.get("/get_books/")
async def get_books_by_author_query(author : str):
    books_list = []
    for books in BOOKS:
        if books.get('author').casefold() == author.casefold():
            books_list.append(books)
    return books_list