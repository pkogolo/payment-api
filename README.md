## Payment Backend 

### Setup

1. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment variables in a `.env` file. You can use the provided `.env.example` file as a template.


3. After setting up the environment variables, you can start the Flask application as mentioned in the `### Usage Local Host` or `### Usage Docker Image` sections.

### Usage Local Host

1. Start the Flask application by running the following command:

   ```bash
   python app.py
   ```

2. The application will start running on [local host](http://localhost:9000). Follow this link in your browser.


### Usage Docker Image

You can also run the application as a Docker container. Follow the steps below to use the Docker image:

1. Create a new file called `Dockerfile` in the project directory.

2. Open the `Dockerfile` and add the following content:

   ```Dockerfile
   # Python3 version used
   FROM python:3.9.17

   # Location of your Flask app
   WORKDIR /app

   # Copy all related files (you can add only specified files e.g.: COPY . /app.py etc)
   COPY . .

   # Install the requirements
   RUN pip install -r requirements.txt

   # Specify a port. The default port for Flask is 5000 if you are not sure what to use or read more about porting.
   EXPOSE 9000

   # This command tells Docker how to run the app
   CMD ["python", "app.py"]
   ```

3. Build the Docker image by running the following command in the project directory:

   ```bash
   docker build -t <any_choice_name> .
   ```

4. Once the image is built, you can run the container using the following command:

   ```bash
   docker run -p 5000:5000 any_choice_name
   ```

5. The application will start running inside the Docker container:  [local host](http://localhost:5000).


Please note that you need to have Docker installed on your machine for the above steps to work.

