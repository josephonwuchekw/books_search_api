from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from mangum import Mangum
import requests
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
base_google_books_url = os.getenv("BASE_GOOGLE_BOOKS_URL")


def fetch_books_by_query(q, filter, start_index,
                         count_per_page, print_type='all',
                         download_format=False, order_by='relevance'):
    filter_values = (
        'partial',
        'full',
        'free-ebooks',
        'paid-ebooks',
        'ebooks'
    )

    print_types = (
        'all',
        'books',
        'magazines'
    )

    sorting_fields = (
        'relevance',
        'newest'
    )

    url = f'{base_google_books_url}?q={q}'

    if filter in filter_values:
        url += f'&filter={filter}'

    if print_type in print_types:
        url += f'&printType={print_type}'

    if order_by in sorting_fields:
        url += f'&orderBy={order_by}'

    if start_index != 0:
        url += f'&startIndex={start_index}'

    if count_per_page != 10:
        url += f'&maxResults={count_per_page}'

    if download_format:
        url += '&download=epub'

    url += f'&key={google_api_key}'

    response = requests.get(url)

    return response.json()


def fetch_book_by_id(book_id):
    url = f'{base_google_books_url}/{book_id}'
    url += f'?key={google_api_key}'
    print(url)
    response = requests.get(url)

    return response.json()


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
