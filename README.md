# Books Search API Application

The Books Search API Application is a RESTful web service that provides endpoints for searching and retrieving information about books. 
This API is built using FastAPI.
It allows users to search for books based on various criteria and retrieve detailed information about each book.

## Features

- **Book Search:** Users can make API requests to search for books using keywords, titles, authors, or any other relevant information.

- **Filtering and Sorting:** The API supports filtering and sorting of search results based on criteria such as relevance and newest

- **Book Details:** Users can retrieve detailed information about a specific book, including its title, author, cover image, and description.

## Technologies Used

- **FastAPI:** A modern web framework for building APIs with Python 3.7+ based on standard Python type hints.

- **Python 3.11:** The programming language used to build the API application logic.

## Installation and Usage

1. Clone this repository to your local machine.
   ```sh
   git clone git@github.com:josephonwuchekw/books_search_api.git

2. Navigate to the project directory.
   ```sh
   cd books_search_api

3. Create and activate a virtual environment (recommended).
   ```sh
   python -m venv venv
   # On Mac or Linux
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate.bat

4. Install the required dependencies using pip.
   ```sh
   pip install -r requirements.txt

5. Run the API server.
   ```sh
   # This runs server at https:127.0.0.1:8000
   uvicorn main:app --reload

6. Open your web browser or API client and navigate to http://localhost:8000/docs to access the API documentation and
test the endpoints using the interactive Swagger UI.


