# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

#install depends
RUN pip install --no-cache-dir -r requirements.txt

#add entrypoint
ENTRYPOINT ["python", "./run.py"]