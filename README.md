# DOST-Exam
**Author:** Andrew Santos

## Part I: Project Overview & Purpose

### Overview

DOST-Exam is a sample Lab Management System developed as part of an entry examination for a contractual role at DOST-ASTI. This project showcases modern technology stack skills by integrating Django for backend operations and Vue.js for frontend development.

### Purpose

This software demonstrates proficiency in:
- **Backend Development:** Utilizing Django for managing server-side logic, database interactions, and API services.
- **Frontend Development:** Leveraging Vue.js to create a responsive and engaging user interface.

### Features

- **Lab Management:** Tools to add, update, search, delete, and show labs.
- **Responsive Interface:** A simple but modern UI built with Vue.js for an enhanced user experience.
- **API Integration:** Seamless communication between the backend and frontend via RESTful APIs.

### Technology Stack

- **Backend:** Django
- **Frontend:** Vue.js
- **Containerization:** Docker

## Part II: Setup & Docker Instructions

### Prerequisites

Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/dost-exam.git
   cd dost-exam
   ```

2. **Start and Initialize the Project:**

    Build and run all services (backend, frontend, and any additional dependencies) using Docker Compose:
    ```bash
    docker-compose up --build
    ```

    This command builds the Docker images and starts the containers as defined in the docker-compose.yml file. It sets up the Django backend, Vue.js frontend, and any related services, such as the database.

3. **Start and Initialize the Project:**

    Once the containers are up and running, open your browser and navigate to the specified local server URLs (usually provided in the docker-compose.yml file or via console output).
