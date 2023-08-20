from fastapi import FastAPI, status, HTTPException
from .fetch_books import fetch_books_by_query, fetch_book_by_id
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API"}


@app.get("/api/v1/books/")
async def get_books(q: str, download_format: str = "",
                    filter: str = "", start_index: int = 0,
                    count_per_page: int = 10, print_type: str = 'all', order_by: str = 'relevance'):
    # fetch books by query
    query_params = (
        q,
        filter,
        start_index,
        count_per_page,
        print_type,
        download_format == 'epub',
        order_by
    )
    result = fetch_books_by_query(*query_params)

    if 'error' in result.keys():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'{result["error"]["message"]}')
    return result


@app.get("/api/v1/book/{book_id}")
async def get_book(book_id):
    result = fetch_book_by_id(book_id)

    if 'error' in result.keys():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'{result["error"]["message"]}')
    return result

handler = Mangum(app=app)
