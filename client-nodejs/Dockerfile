# Use the official Node.js image from the Docker Hub
FROM node:20-slim

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY client-nodejs/package.json client-nodejs/package-lock.json ./
COPY protos ./protos

# Install dependencies
RUN npm install

# Copy the client code into the container
COPY client-nodejs/client.js .

# Command to run the client when the container starts
CMD [ "npm", "start" ]
#CMD ["/bin/bash"]
