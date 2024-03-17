# Project Gutenberg Books API

This API provides access to books available in Project Gutenberg, a repository of freely available e-books.

## Getting Started

To get started with using this API, follow the instructions below:

### Installation

1. Clone the repository to your local machine:

   git clone git@github.com:AbhaySatpute/book_api_project.git


## Create the virtual enviroment to install the packages

## for ubuntu os 

   virtualenv virenv


## activate virtual enviroment for ubuntu

   source virenv/bin/activate



## for windows

   py -m venv virenv



## activate virtual enviroment for windows

   virenv\Scripts\activate.bat 



## Install the required Python packages:

   pip install -r requirements.txt



## Run the Django development server:

   python manage.py runserver



The API will be accessible at http://127.0.0.1:8000/books/




## Endpoints
## Get Books

    URL: /books/
    Method: GET
    Description: Retrieves a list of books based on optional filter criteria.
    Parameters:
        language: Filter books by language (comma-separated list for multiple languages).
        topic: Filter books by topic (subject or bookshelf) (comma-separated list for multiple topics).
        author: Filter books by author (partial match).
        title: Filter books by title (partial match).



Example:

    Retrieve books in English by Charles Dickens:

    GET /books/?language=en&author=Dickens



Pagination

    The API returns a maximum of 20 books per page.
    Use the page query parameter to navigate through pages.




Response Format

The API returns a JSON object containing a list of books. Each book object includes the following fields:

    title: Title of the book.
    author: Author of the book.
    language: Language of the book.
    download_count: Number of downloads.
    bookshelf_name: Bookshelf name.
    mime_type: Mime type.
    url: URL to download the book.
    subject: Subject of the book.




