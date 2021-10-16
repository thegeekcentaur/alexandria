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
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# route-specific modules go here
from api.routes import urls
from core import database
from typing import Optional
from models.schemas.catalog import (
    CatalogSchema
)

router = APIRouter()

# Catalog APIs Added by ArchanaTBits


# saving the catalog data to mongodb..
@router.post(urls.create_catalog_url)
async def create_catalog(catalog_data: CatalogSchema = Body(...)):
    new_entry = await database.create_catalog(catalog_data)
    return {"new catalog": new_entry}


# Added by ArchanaTBits
# Search Catalog
@router.get(urls.get_all_catalogs_of_user_url)
async def get_all_catalogs_of_user(user_id : str, catalog_name : str):
    try:
        logger.info("Fetching Catalog details :".format(catalog_name))
        print("Fetching Catalog details :")
        catalog_item = await database.get_all_catalogs_of_user(user_id, catalog_name)
        print("catalog_item")
        print(catalog_item)
        if catalog_item:
            return catalog_item
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"catalog_item": catalog_item,
            "message": "Catalog not found for given search string"}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Updating the existing catalog books data
@router.put(urls.update_books_to_catalog_url)
async def update_books_to_catalog( user_id : str, catalog_name: str ,books_list: list[str]):
    logger.info("Adding book for the catalog {}".format(catalog_name))
    try:
        catalog_updated = await database.update_catalog_book_list(user_id, catalog_name, books_list)
        if catalog_updated:
            return {"Books Updated Successfully to the Catalog {}".format(catalog_name)}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Getting books of a catalog from mongodb...
@router.get(urls.get_books_of_catalog_url)
async def get_books_of_catalog(user_id : str, catalog_name: str):
    logger.info("Fetching catalog details for the ID {}".format(catalog_name))
    try:
        catalog_found = await database.get_all_catalogs_of_user(user_id, catalog_name)
        if catalog_found:
            return {"books": catalog_found["books"]}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Deleting catalog data
@router.delete(urls.delete_catalog_by_name_url)
async def delete_catalog_by_name(user_id : str, catalog_name: str):
    try:
        catalog_deleted = await database.delete_catalog(user_id,catalog_name)
        if catalog_deleted:
            return {"name": catalog_name, "message": "Deletion successful"}
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message

# Deleting books from catalog
@router.put(urls.delete_catalog_by_name_url)
async def delete_books_from_catalog(user_id : str, catalog_name: str, books_remove_list: list):
            try:
                catalog_updated = await database.delete_books_from_catalog(user_id,catalog_name,books_remove_list)
                if catalog_updated:
                    return {"name": catalog_name, "message": "Deletion of books from catalog is successful"}
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                return message

# Getting list of catalogs from mongodb...
@router.get(urls.get_all_catalogs_url)
async def get_catalog_list(user_id: Optional[str] = None):
    if user_id:
        catalogs = await database.retrieve_catalogs_for_user(user_id)
    else:
        catalogs = await database.retrieve_catalogs()
    return {"catalogs": catalogs, "totalcatalogs": len(catalogs)}

# Render welcome message
@router.get('/', response_class=HTMLResponse)
async def catalog_management(response: Response, request: Request):
    return "Welcome to catalog management, coming soon"
