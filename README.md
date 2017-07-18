# Rostelekom_task
```
docker run -p 80:80 -v /path/to/csv:/app/get_server_app/uploads -v /path/to/fullchain.pem:/app/fullchain.pem -v /path/to/privkey.pem:/app/privkey.pem server
```

**/get_server** - get-server dir
#
```
docker run -v /path/to/csv:/app/uploads -v /path/to/pdfs:/app/download_pdfs hash_searcher
```

**/hash_searcher** - application for search hashes and create .csv