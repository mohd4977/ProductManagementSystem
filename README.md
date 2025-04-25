# Product Management System

---

## Description

Welcome to the **Product Management System**! This project is a comprehensive application built with **Python**, **Django**, **Django REST Framework (DRF)**, and **Celery**. It manages products. The application is fully containerized using **Docker**, allowing for easy setup and deployment. Whether you're a developer looking to explore the project or setting it up for development purposes, this README will guide you through the necessary steps.

## Technologies Used

- **Python 3.9**
- **Django 4.2**
- **Django REST Framework**
- **Celery 5.3**
- **Redis 6**
- **Docker & Docker Compose**

## Features

- **Product Management**: Create, read, update, and delete products.
- **API Endpoints**: CRUD operations for all models using Django REST Framework.
- **Celery Tasks**: Celery tasks for updating products .
- **Admin Interface**: Django admin panel for data management and for bulk updates to product prices.
- **Webhook Endpoint**: Webhook endpoint to handle inventory updates from Shopify.
- **User Authentication**
- **Docker-Ready**: Easy setup and deployment using Docker and Docker Compose.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mohd4977/ProductManagementSystem.git 
   
   # If you dont have a prefered version control, we recommend https://github.com/new (free)
   git remote rename origin upstream
   git remote add origin [URL of your newly created repo: https://github.com/...]
   git push -u origin main
   ```

2. **Create a `.env` File**

   In the root directory, create a `.env` file to store environment variables.

   ```bash
   touch .env
   ```

   **Content of `.env`:**

   ```env
   # .env
   DEBUG=1
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   CELERY_BROKER_URL=redis://redis:6379/0
   CELERY_RESULT_BACKEND=redis://redis:6379/0
   SECRET_KEY=your-secret-key
   DEFAULT_FROM_EMAIL=admin@library.com
   ```

   > **Note:** Replace `your-secret-key` with a secure key. Ensure that `.env` is included in `.gitignore` to prevent committing sensitive information.

3. **Build and Run Docker Containers**

   ```bash
   docker-compose build
   docker-compose up
   ```

   This command will:
   - Start Redis (`redis`) services.
   - Build and run the Django application (`web`).
   - Run the Celery worker (`celery`).

4. **Initialize the Django Project**

   In a separate terminal, apply migrations and create a superuser.

   ```bash
   docker-compose run web python manage.py makemigrations
   docker-compose run web python manage.py migrate
   docker-compose run web python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.
   login to admin panel
   add inventory_managers group in admin

### Running the Project

Start all services with Docker Compose:

```bash
docker-compose up
```

**Stopping the Services:**

To stop the running containers, press `CTRL+C` in the terminal where `docker-compose up` is running, then execute:

```bash
docker-compose down
```

## Accessing the Application

### Django Admin Interface

- **URL:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Login:** Use the superuser credentials you created during setup.
- **Functionality:** Manage authors, books, members, and loans through the admin panel.

### API Endpoints

- **Base URL:** [http://localhost:8000/api/](http://localhost:8000/api/)
- **Endpoints:**
  - `/api/products/`: CRUD operations for authors.
  - `/api/webhooks/shopify/inventory/`: Shopify invertory updates.
- **Access:** Use tools like **Postman**, **cURL**, or the DRF browsable API to interact with the endpoints.

## 🗃️ Database Schema

### Product Model
- `name`: CharField
- `sku`: CharField (unique)
- `price`: DecimalField
- `inventory_quantity`: IntegerField
- `last_updated`: DateTimeField (auto-updated)

