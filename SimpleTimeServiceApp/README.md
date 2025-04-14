# SimpleTimeService
A simple microservice returning timestamp and client IP.

## Run locally:
```bash
docker build -t your-dockerhub-username/simpletimeservice .
docker run -p 5000:5000 your-dockerhub-username/simpletimeservice
