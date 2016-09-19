#Getting started with docker-compose, using python/flask & redis

There is a basic python flask web app in `app.py`, a Dockerfile for the specs of the container for that app (which is based off a python image), a requirements file for Docker installation additional requirements for the app (flask, redis), and a docker-compose file for the specification of the composed containers which includes the flask and redis containers. 

1. Create the files locally and look to see what each one does. 

1. Run `docker-compose build' to build the containers specified in the docker-compose file.

1. Run `docker-compose up` to start the containers (add -d to run them in the background. Then run `docker-compose stop` when done.)  