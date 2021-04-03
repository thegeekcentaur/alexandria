__author__ = 'surendar'
__date__ = '01-Apr-2021'
__copyright__ = "Copyright 2021"
__credits__ = ["surendar"]
__license__ = "All rights reserved"
__version__ = "0.1"
__maintainer__ = "surendar"
__email__ = "2020mt93162@wilp.bits-pilani.ac.in"
__status__ = "dev"

from fastapi import FastAPI
from typing import Optional
import requests

app = FastAPI(debug=True)

URL = 'https://www.googleapis.com/books/v1/volumes'

def get_books_by_isbn(isbn: str):
    PARAMS = {'q': 'isbn' + isbn}
    get_book = requests.get(url=URL, params=PARAMS)
    return get_book.json()