import json
import requests

# local
from api.routes import urls
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def collection_insert_record(service_name, ds_item) -> str:
    """
    Used to insert record based on the registered service name in db-service

    :param kpi_res_list:
    :type str,list:
    :return str(success message for insertion):
                                                    """
    req_body = json.dumps(ds_item, indent=4)
    try:
        logger.info("in post...")
    except ConnectionError as err:
        logger.error("db service connection failed for inserting record: {}".format(err))
        return {"status": False, "message": "Db service connection failed"}
    if db_id_res.status_code != 200:
        return {"status": False, "message": "Db service failed to insert record"}
    db_id_res = db_id_res.json()
    return db_id_res


def query_check(book_name):
    """
    Used to query a particular record based on the registered service name in db-service.

    :param book_name:
    :type str,dict:
    :return success response from db-service:
                                                        """

    req_body = json.dumps(book_name, indent=4)
    try:
        logger.info("in post...")
    except ConnectionError as e:
        logger.error("db service connection failed for querying record: {}".format(err))
        return {"status": False, "message": "Db service connection failed"}
    db_id_res = db_id_res.json()
    try:
        if not db_id_res.get("data"):
            return None
        else:
            return db_id_res.get("data")
    except TypeError as te:
        logger.error("Error occurred in query response: {}".format(te))


def delete_record(service_name, ds_item_body):
    """
    Used to delete a particular record based on the registered service name in db-service.

    :param service_name,ds_item_body:
    :type str,dict:
    :return boolean:
                                                            """
    req_body = json.dumps(ds_item_body, indent=4)
    try:
        #db_id_res = requests.delete(urls.db_service_reg + service_name, data=req_body)
        logger.info("in delete...")
    except ConnectionError as e:
        logger.error("db service connection failed for deleting record: {}".format(err))
        return {"status": False, "message": "Db service connection failed"}
    if db_id_res.status_code == 200:
        return True
    else:
        return False


def update_record(service_name, ds_item_body):
    """
    Used to update a particular record based on the registered service name in db-service.

    :param service_name,ds_item_body:
    :type str,dict:
    :return boolean:
                                                                """
    req_body = json.dumps(ds_item_body, indent=4)
    try:
        #db_id_res = requests.put(urls.db_service_reg + service_name, data=req_body)
        logger.info("in put...")
    except ConnectionError as e:
        logger.error("db service connection failed for updating record: {}".format(err))
        return {"status": False, "message": "Db service connection failed"}
    db_id_res = db_id_res.json()
    if db_id_res.get("data") == "1":
        return True
    else:
        return False
