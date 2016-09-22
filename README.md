# flask-angular2-starter

Starter app with a simple flask backend, and an Angular2 frontend. Somewhat opinionated. Full docker support, webpack, hot module reload, and more.

## Application Structure

1.  `/src/server` directory contains the flask backend with simple authentication methods

2.  `/src/client` directory contains the angular2 frontend based on  [angular-webpack-starter](https://github.com/AngularClass/angular2-webpack-starter)

## Setup Instructions

Clone the repo

    ```bash
    git clone --depth 1 https://github.com/cacois/flask-angular2-starter.git
    cd flask-angular2-starter
    ```

Set your local env variable FLASK_CONFIGURATION to "development" if you plan on using Docker or command line:

    ```bash
    export FLASK_CONFIGURATION=development
    ```

Or set it to "ide_development" if you wnat to use an IDE with step-through debugger:

    ```bash
    export FLASK_CONFIGURATION=ide_development
    ```

### Running using Docker

The app runs in two Docker containers, one for the Flask server, and one for the Angular2 client. Use docker-compose to build and stand up both containers:

    ```bash
    docker-compose up
    ```

Note: The FLASK_CONFIGURATION environment variable will be picked up from your host machine and passed through to the Flask container, setting the server configuration mode.

### Running locally

#### Flask Backend

Install necessary Python modules:

    ```bash
    cd src/server
    sudo pip install -r requirements.txt
    ```

Launch the backend app locally:

    python run.py

Or through your IDE.

To test the Flask API manually, navigate to http://localhost:8081/api/test

#### Angular2 Frontend

Install frontend dependencies:

If you don't have it already, install Node.js. [nvm](https://github.com/creationix/nvm) is a great solution to manage Node.js installations

Now install dependencies using NPM:    

    ```bash
    cd src/client

    # install global dependencies
    npm install webpack-dev-server rimraf webpack typescript -g

    # install project related dependencies
    npm install
    ```

And launch the Angular2 frontend app:

    npm run server:dev:hmr


You can now navigate to `http://localhost:3000`. Login with default credentials : `admin:admin`

### Docker support:

1. Build the docker backend

  ```bash
  cd backend
  docker build --no-cache  -t backend/python:latest .
  docker run -it -p 8081:8081 --name server backend/python
  ```
  To connect to the running container:
  ```bash
  docker exec -it server /bin/sh
  ```
2. Build the frontend

  ```bash
  cd front
  docker build --no-cache  -t frontend/angular2:latest .
  docker run -it -p 3000:8080 --name angular2-app frontend/angular2
  ```

3. Navigate to `http://localhost:3000`  

4. Easiest way to run this application to run `docker-compose up` in the project root directory.
