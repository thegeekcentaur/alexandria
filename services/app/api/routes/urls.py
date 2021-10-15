__author__ = 'archanda'
__date__ = '31-Mar-2021'
__copyright__ = "Copyright 2021"
__credits__ = ["archanda"]
__license__ = "All rights reserved"
__version__ = "0.1"
__maintainer__ = "archanda"
__email__ = "2020mt93064@wilp.bits-pilani.ac.in"
__status__ = "dev"

save_book_url="/api/books/local"
get_book_by_id_url="/api/books/local/id/{book_id}"
# Added by ArchanaTBits
update_book_by_id_url="/api/books/local/id/{book_id}"
delete_book_by_id_url = "/api/books/local/id/{book_id}"
get_all_books_url="/api/books/local/all"
get_book_details_by_isbn = "/api/books/isbn/{isbn}"
get_book_details_by_author = "/api/books/author/{author_name}"
get_book_details_by_genre = "/api/books/genre/{genre}"
# Added by Surabhi
get_book_details_by_publisher = "/api/books/publishers/{publisher_name}"

# Added by ArchanaTBits
#Catalog APIs
create_catalog_url="/api/catalogs/local"
add_book_to_catalog_url="/api/catalogs/local/name/{catalog_name}/{book_id}"
update_books_to_catalog_url = "/api/catalogs/local/name/{catalog_name}/books"
delete_books_from_catalog_url = "/api/catalogs/local/name/{catalog_name}/books"
get_all_catalogs_of_user_url="/api/catalogs/local/name/{catalog_name}"
get_books_of_catalog_url="/api/catalogs/local/books"
delete_catalog_by_name_url="/api/catalogs/local/name/{catalog_name}"
get_all_catalogs_url="/api/catalogs/local/all"

#Added By Surendar S BITs
#User Management APIs
get_all_users_url = "/api/user/local/all"
get_all_user_by_id_url = "/api/user/local/id/{user_id}"
save_user_url = "/api/user/local"
update_user_by_id_url = "/api/user/local/id/{user_id}"
delete_user_by_id_url = "/api/user/local/id/{user_id}"

#Search Books by user impersonation
search_book_by_user_id = "/api/user/{user_id}/book/search"

#APIs to perfrom catalog CRUD operations by user impersonation
get_all_catalog_for_user_id = "/api/user/{user_id}/catalog"
get_catalog_by_name_for_user_id = "/api/user/{user_id}/catalog/{catalog_name}"
save_catalog_by_user_id = "/api/user/{user_id}/catalog/"
update_catalog_by_name_for_user_id = "/api/user/{user_id}/catalog/{catalog_name}"
delete_catalog_by_name_for_user_id = "/api/user/{user_id}/catalog/{catalog_name}"