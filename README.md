# Getting started with docker-compose, using python/flask & redis

Compose is a tool for defining and running multi-container Docker applications. You use a Compose file to configure your application’s services. Then using a single command, you create and start all the services.

In this repo, there is a basic python flask web app in `app.py`, a Dockerfile for the specs of the container for that app (which is based off a python image), a requirements file for Docker installation additional requirements for the app (flask, redis), and a docker-compose file for the specification of the composed containers which includes the flask and redis containers. I created this in conjunction with reading this docker-compose tutorial, so you can use it to get more information on what these files do, https://docs.docker.com/compose/gettingstarted/

To get the app running in one container with redis in another, try these steps:

1. Create the files locally. See if you can tell what each one does. Check the above link to learn more.

1. Run `docker-compose build' to build the containers specified in the docker-compose file.

1. Run `docker-compose up` to start the containers (add -d to run them in the background. Then run `docker-compose stop` when done.)  

1. Browse to http://localhost:5000 to see the response from the web app. 
