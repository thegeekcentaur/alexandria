# Disclaimer
**This is a directory to keep the microservices**

# Run/Set-up
```console
docker build -t local/alexandria:1.0.003 . --no-cache
```

# Goal/Objective

We would be spinning up the Books Service and its related dependencies here:

```console
docker-compose up
```

1. You may check the API documentation by hitting http://localhost:9000/docs from your browser
1. It will start two containers 1. Books micro service 2. MongoDB
1. It takes the port number 9000 configured in the Dockerfile.




# Below are the services currently available

Book APIs
1. Save a New Book: /api/books/local
2. Update an Existing Book: /api/books/local/id/{book_id}
3. Get Book Details using Book Id: /api/books/local/id/{book_id}
4. Get Book Details using Book ISBN: /api/books/isbn/{isbn}
5. Get Book Details by Author Name: /api/books/author/{author_name}
6. Get Book Details by Genre: /api/books/genre/{genre}
7. Delete a Book Instance by its Id: /api/books/local/id/{book_id}
8. Get all the Books Available : /api/books/local/all
9. Get all Books by Publisher : /api/books/publishers/{publisher_name}

Catalog APIs
1. Create New Catalog: "/api/catalogs/local"
2. Add a book to catalog: "/api/catalogs/local/name/{catalog_name}/{book_id}"
3. Get Catalog Details using name:"/api/catalogs/local/name/{catalog_name}"
4. Get All Books of a Catalog: "/api/catalogs/local/books"
5. Delete a Catalog by name: "/api/catalogs/local/name/{catalog_name}"
6. Get all Catalogs : "/api/catalogs/local/all"


# Tips for implementing a new service
1. Add URL Path in the **urls.py**
2. Tag the URL path in an annotation of respective api definition in **main.py**
3. Implement DB operation ( any of CURD operations ) in **database.py** if required
4. Call the above implemented DB operation in api definition of  **main.py**


# License

ISC
