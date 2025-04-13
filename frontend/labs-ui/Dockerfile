# Use an official Node.js runtime as a parent image
FROM node:23.11.0

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY package.json /app/
COPY package-lock.json /app/
RUN npm install

# Copy the rest of the application
COPY . /app/

# Expose the port that the Vue app runs on
EXPOSE 8080

# Run the Vue application
CMD ["npm", "run", "dev", "--host"]
