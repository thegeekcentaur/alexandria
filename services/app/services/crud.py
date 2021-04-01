__author__ = 'archanda'
__date__ = '31-Mar-2021'
__copyright__ = "Copyright 2021"
__credits__ = ["archanda"]
__license__ = "All rights reserved"
__maintainer__ = "Guardians Of The Galaxy"
__email__ = "2020mt93064@wilp.bits-pilani.ac.in"
__status__ = "dev"

from datetime import datetime, timezone
from bson.objectid import ObjectId
from pymongo import ReturnDocument

# local
from api.errors.errors import invalid_request
from common import getenv
from core.database import db, collection
from common.utils import collection_insert_record, query_check, update_record, delete_record
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def save_book(book_data):
    """
               Used to save book in mongodb...

               :param book_data:
               :type dict:
               :return book_id generated after saving book in mongodb:
    """
    if book_data:
        try:
            dboard_name_body = {"name": book_data.get("name")}
            logger.debug("Saving book: {}".format(dboard_name_body))
            dboard_name_check = query_check(getenv.SERVICE_NAME, dboard_name_body)
            if dboard_name_check is None:
                try:
                    if "name" in book_data:
                        if book_data.get("name").isspace() or len(book_data.get("name")) == 0:
                            return False
                    else:
                        return False
                    book_data["created_on"] = (datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M:%S%z")
                    book_data["updated_on"] = ""
                    resp_insert = collection_insert_record(getenv.SERVICE_NAME, book_data)
                    if resp_insert:
                        return resp_insert
                    else:
                        return {"status": False,
                                "message": "Failed to insert dataset item"}
                except Exception as err:
                    invalid_request(err)
                    return False
            else:
                return {"status": False, "message": "Book name " + book_data.get("name") + " already exists."}
        except Exception as err:
            invalid_request(err)
            return False


def getbook_list():
    """
               Used to list book from mongodb

               :returns all book items from mongodb:
    """
    get_items = []
    try:
        db_name_all = query_check(getenv.SERVICE_NAME, {})
        logger.debug("List all books: {}".format(db_name_all))
        if db_name_all:
            for item in db_name_all:
                item['_id'] = item.get("id")
                item.pop("id", None)
                get_items.append(item)
    except Exception as err:
        logger.error(err)
        return get_items
    return get_items


def getbook_Data(dboard_id):
    """
                  Used to get the book data based on book id..

                  :param dboard_id:
                  :type str:
                  :return book items based on book id:
           """
    try:
        dboard_id_body = {"id": dboard_id}
        logger.debug("Listing book with id: {}".format(dboard_id_body))
        item = query_check(getenv.SERVICE_NAME, dboard_id_body)
        if item:
            item['_id'] = str(item['id'])
            item.pop('id')
            return item
    except Exception as err:
        logger.error(err)
        return False


def update_Book(dboard_id, updated_book_data):
    """
                           Used to update a book based on dataset id

                           :param dboard_id,updated_book_data:
                           :type str,dict:
                           :return updated book item:
                    """
    try:
        updated_book_data["updated_on"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S%z")
        dboard_id_body = {"id": dboard_id}
        logger.debug("Updating book with id: {}".format(dboard_id_body))
        book_collection = query_check(getenv.SERVICE_NAME, dboard_id_body)
        if book_collection:
            if "name" in updated_book_data:
                if updated_book_data.get("name").isspace() or len(updated_book_data.get("name")) == 0:
                    return {"status": False, "message": "InvalidParams"}
            updated_book_data["id"] = dboard_id
            update_rec = update_record(getenv.SERVICE_NAME, updated_book_data)
        if update_rec:
            return updated_book_data
        else:
            return update_rec
    except Exception as err:
        logger.error(err)
        return False


def delete_Book(dboard_id):
    """
                               Used to delete a book based on book id

                               :param dboard_id:
                               :type str:
                               :return boolean:
                        """
    try:
        dboard_id_body = {"id": dboard_id}
        logger.debug("Deleting book with id: {}".format(dboard_id_body))
        dboard_del = delete_record(getenv.SERVICE_NAME, dboard_id_body)
        logger.debug(dboard_del)
        return dboard_del
    except Exception as err:
        logger.error(err)
        return False
