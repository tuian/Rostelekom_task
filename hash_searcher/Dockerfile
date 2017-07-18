# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

#install depends
RUN pip install --no-cache-dir -r requirements.txt

#bug lib
RUN CFLAGS="-O0" pip install lxml==3.6.4

RUN apt-get update -y

RUN apt-get install -y poppler-utils

#add entrypoint
ENTRYPOINT ["python", "./main.py"]