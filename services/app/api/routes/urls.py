__author__ = 'archanda'
__date__ = '31-Mar-2021'
__copyright__ = "Copyright 2021"
__credits__ = ["archanda"]
__license__ = "All rights reserved"
__version__ = "0.1"
__maintainer__ = "archanda"
__email__ = "2020mt93064@wilp.bits-pilani.ac.in"
__status__ = "dev"

#local
from common import getenv

save_book="/api/book"
getbookNames_url="/api/book"
getbook_url="/api/book"
updatebook_url="/api/book"
deletebook_url = "/api/book"
get_book_details_by_isbn = "/api/books/isbn/{isbn}"
get_book_details_by_author = "/api/books/author/{author_name}"
get_book_details_by_genre = "/api/books/genre/{genre}"

#db_service_reg=getenv.DB_SERVICE_URL