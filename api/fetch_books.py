from dotenv import load_dotenv
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
