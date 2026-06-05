# Inventory Management System

## Project Overview

This project is a full-stack Inventory Management System developed using React, FastAPI, PostgreSQL, Docker, and Docker Compose.

The system allows users to manage products, customers, and orders while automatically updating inventory levels.

## Features

### Product Management

* Add Product
* View Products
* Update Product
* Delete Product
* SKU Validation

### Customer Management

* Add Customer
* View Customers
* Delete Customer
* Email Validation

### Order Management

* Create Orders
* View Orders
* Automatic Stock Reduction
* Inventory Availability Check

### Dashboard

* Total Products
* Total Customers
* Total Orders
* Low Stock Products

## Technologies Used

### Frontend

* React
* React Router
* Axios
* Tailwind CSS

### Backend

* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### Containerization

* Docker
* Docker Compose

## Project Structure

backend/

* FastAPI Backend
* SQLAlchemy Models
* API Endpoints

frontend/

* React Frontend
* Dashboard
* Product Management
* Customer Management
* Order Management

## API Endpoints

### Products

* GET /products
* POST /products
* PUT /products/{id}
* DELETE /products/{id}

### Customers

* GET /customers
* POST /customers
* DELETE /customers/{id}

### Orders

* GET /orders
* POST /orders
* DELETE /orders/{id}

### Dashboard

* GET /dashboard

## Running the Project

### Using Docker

```bash
docker compose up --build
```

### Frontend

http://localhost:5173

### Backend

http://localhost:8000

### Swagger Documentation

http://localhost:8000/docs


