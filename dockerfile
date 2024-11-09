# sets the base image for your Docker image, online 
FROM python:3.10-slim-buster  

# sets the working directory inside the Docker container to /app. name of container
WORKDIR /app

# copies the requirements.txt file from your local machine into the 
#/app directory inside the Docker container.
COPY requirements.txt requirements.txt

# runs the command to install all Python dependencies listed in requirements.txt
# using pip3 
RUN pip3 install -r requirements.txt

# This copies all files and directories from your current local 
# directory to the /app directory in the Docker container.
COPY . .

#This tells Docker that the container will listen on port 5000 at runtime
EXPOSE 5001

#command to run when the container starts
#runs python3 to execute the Flask application using the -m module flag,
# with options to run the app and bind it to all network interfaces (--host=0.0.0.0).
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]