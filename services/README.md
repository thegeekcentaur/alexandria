# Disclaimer
**This is a directory to keep the microservices**

# Run/Set-up
```console
docker build -t local/alexandria:1.0.000 . --no-cache
```

# Goal/Objective

We would be spinning up the Books Service and its related dependencies here:

```console
docker-compose up -d
docker run -e PORT=9000 -p 9000:9000 local/alexandria:1.0.000
```

It will start two containers 1. Books micro service 2. MongoDB
It takes the port number 4008 configured in the Dockerfile.