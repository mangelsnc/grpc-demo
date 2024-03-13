# Use the official Python image from the Docker Hub
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY client-python/requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy all files from the current directory into the container
COPY client-python/* .
COPY protos ./protos

# Compile proto files
RUN python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. exchange.proto

# Command to run the gRPC server when the container starts
CMD [ "python3", "client.py" ]
