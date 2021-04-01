# local
from common.utils import query_check
from common import getenv
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def searchTerm(q):
    """
    Used to perform search operation for a particular object or list of objects based on search term received as query parameter.

    :param q:
    :type str:
    :return list of objects:
                """
    try:
        ds_id_body = {"name": {"$regex": q}}
        items = query_check(getenv.SERVICE_NAME, ds_id_body)
        return items
    except Exception as err:
        logger.error("Exception occurred: {}".format(err))


def pageLimit(get_items, page, limit):
    """
    Used to perform pagination for the given list of objects based on page number and limit received as query parameters.

    :param get_items,page,limit:
    :type list,int,int:
    :return list of objects and also the number of records for the particular page number.:
                """
    try:
        start = (limit * (page - 1))
        stop = (limit * page)
        if start >= len(get_items):
            tmp_list = []
            return tmp_list, len(tmp_list)
        elif stop >= len(get_items):
            stop = len(get_items)
            return get_items[start:stop], len(get_items)

        return get_items[start:stop], len(get_items)
    except Exception as err:
        logger.error("Exception occurred: {}".format(err))
