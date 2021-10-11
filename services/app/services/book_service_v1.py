__author__ = 'archanda'
__date__ = '3-Oct-2021'
__copyright__ = "Copyright 2021"
__credits__ = ["archanda"]
__license__ = "All rights reserved"
__maintainer__ = "archanda"
__email__ = "2020mt93064@wilp.bits-pilani.ac.in"
__status__ = "dev"

from fastapi import FastAPI, Body, APIRouter, Request, Response, status
from fastapi.responses import HTMLResponse
import logging
from core import database
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# route-specific modules go here
from api.routes import urls

from models.schemas.book import (
    BookSchema
)

router = APIRouter()

# saving the book data to mongodb..
@router.post(urls.save_book_url)
async def save_book(book_data: BookSchema = Body(...)):
    new_entry = await database.add_book(book_data)
    return {"new book": new_entry}


# Added by ArchanaTBits
# Updating the existing book data
@router.put(urls.update_book_by_id_url)
async def update_book_details_by_id(book_id: str, book_data: BookSchema = Body(...)):
    logger.info("Updating Book details for the Book Id {}".format(book_id))
    try:
        book_updated = await database.update_book_by_id(book_id, book_data)
        if book_updated:
            return {"Book Updated  Successfully {}": book_id}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Getting book by id from mongodb...
@router.get(urls.get_book_by_id_url)
async def get_book_by_id(book_id: str):
    logger.info("Fetching Book details for the ID {}".format(book_id))
    try:
        book_found = await database.get_book(book_id)
        if book_found:
            return {"book": book_found}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Deleting book data
@router.delete(urls.delete_book_by_id_url)
async def delete_book_by_id(book_id: str):
    try:
        book_deleted = await database.delete_book(book_id)
        if book_deleted:
            return {"id": book_id, "message": "Deletion successful"}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Getting list of books from mongodb...
@router.get(urls.get_all_books_url)
async def get_book_list():
    books = await database.retrieve_books()
    return {"books": books, "totalBooks": len(books)}

# Fetching book by ISBN...
@router.get(urls.get_book_details_by_isbn)
async def get_books_by_isbn(isbn):
    try:
        logger.info("Fetching Book details for the ISBN {}".format(isbn))
        item = book_details_module.get_books_by_filter('isbn', isbn)
        if item:
            return item
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"isbn": isbn,
            "message": "book not found for given ISBN"}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Fetching book by Author name...
@router.get(urls.get_book_details_by_author)
async def get_books_by_author(author_name):
    try:
        logger.info("Fetching Book details for the Author Name: \"{}\"".format(author_name))
        item = book_details_module.get_books_by_filter('inauthor', author_name)
        if item:
            return item
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"author": author_name,
            "message": "Either invalid author name or book not found for given Author Name"}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Fetching book by genre...
@router.get(urls.get_book_details_by_genre)
async def get_books_by_genre(genre):
    logger.info("Fetching Book details for the genre: \"{}\"".format(genre))
    try:
        item = book_details_module.get_books_by_filter('subject', genre)
        if item:
            return item
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"genre": genre,
            "message": "Either invalid genre or book not found for given genre"}
    except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                return message


# Fetching book by Publisher...
@router.get(urls.get_book_details_by_publisher)
async def get_books_by_publisher(publisher_name):
    logger.info("Fetching Book details for the publisher: \"{}\"".format(publisher_name))
    try:
        item = book_details_module.get_books_by_filter('inpublisher', publisher_name)
        if item:
            return item
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"publisher": publisher_name,
            "message": "Either invalid publisher or book not found for given publisher"}
    except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                return message

# Render welcome message
@router.get('/', response_class=HTMLResponse)
async def books_search(response: Response, request: Request):
    return "Welcome to books search, powered by Google Books API"
