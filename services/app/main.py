__author__ = 'archanda'
__date__ = '31-Mar-2021'
__copyright__ = "Copyright 2021"
__credits__ = ["archanda"]
__license__ = "All rights reserved"
__maintainer__ = "archanda"
__email__ = "2020mt93064@wilp.bits-pilani.ac.in"
__status__ = "dev"

from fastapi import FastAPI
from fastapi import Response, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
# local
from api.routes import urls
from common.lib import searchTerm, pageLimit
from common import getenv
from core.database import db, collection
from services import crud


app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# saving the book data to mongodb..
@app.post(urls.save_book)
async def saveBook(response: Response, book_data: dict):
    response_check = crud.save_book(book_data)
    if response_check:
        if "status" in list(response_check.keys()) and "message" in list(response_check.keys()):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": response_check.get("message")}
        else:
            response.status_code = status.HTTP_201_CREATED
            return {"book_id": response_check.get("data"),
                    "message": "book Created successfully"}
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "Request body does not contain any valid parameters."}


# Getting list of books from mongodb...
@app.get(urls.getbookNames_url)
async def getBookList(response: Response, q: Optional[str] = None, page: Optional[int] = None,
                           limit: Optional[int] = None):
    get_items = crud.getbook_list()
    # search term..
    if q:
        get_items = searchTerm(q)
        if get_items is None:
            get_items = []
    # pagination logic..
    if page and limit:
        records_lst, total_records = pageLimit(get_items, page, limit)
        return {"book_list": records_lst, "totalrecords": total_records}
    if get_items:
        return {"book_list": get_items, "totalrecords": len(get_items)}
    return {"book_list": get_items, "totalrecords": len(get_items)}


# Getting book data from mongodb...
@app.get(urls.getbook_url)
async def getBookData(response: Response, dboard_id: str):
    item = crud.getbook_Data(dboard_id)
    if item:
        return item
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"book_id": dboard_id,
            "message": "book Id not found in DB"}


# Updating book data
@app.put(urls.updatebook_url)
async def updateBook(response: Response, dboard_id: str, updated_book_data: dict):
    new_query_dict = crud.update_Book(dboard_id, updated_book_data)
    if new_query_dict:
        if new_query_dict["status"]:
            return {"book_id": dboard_id,
                    "message": "Book updated successfully",
                    "updated_response": new_query_dict}
        else:
            if new_query_dict["message"] == "InvalidID":
                return {"book_id": dboard_id,
                        "message": "Book Id not found in DB"}
            else:
                return {"book_id": dboard_id,
                        "message": "Request body does not contain any valid parameters."}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"book_id": dboard_id,
            "message": "Something went wrong while updating book"}


# Deleting book data
@app.delete(urls.deletebook_url)
async def deleteBook(response: Response, dboard_id: str):
    response_check = crud.delete_Book(dboard_id)
    if response_check:
        response.status_code = status.HTTP_204_NO_CONTENT
        return {"book_id": dboard_id,
                "message": "Book Deleted Successfully"}

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"book_id": dboard_id,
            "message": "Book Id not found in DB"}
