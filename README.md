Recipe API Backend Application 🍳
A robust, scalable backend API for a recipe management application built with Django REST Framework and modern technologies.
🌟 Features

Advanced REST API Architecture

Complete CRUD operations using ViewSets
Custom endpoints with APIViews
Complex data modeling with nested serializers


Performance Optimization

Redis caching for frequently accessed recipes
Rate limiting on API endpoints
Response caching using Python decorators


Scalable Infrastructure

Kubernetes container orchestration
Docker containerization
Apache Kafka for real-time event handling


Security & Authentication

Custom user authentication system
Secure user profile management
Protected API endpoints



🛠️ Technology Stack

Backend Framework: Django REST Framework
Database: PostgreSQL
Caching: Redis
Container Technology: Docker, Docker-Compose
Container Orchestration: Kubernetes
Message Broker: Apache Kafka
Web Server: Nginx
Programming Language: Python

🏗️ Architecture
The application is built with a microservices architecture using Docker containers:

Django REST API container
PostgreSQL database container
Nginx reverse proxy container
Redis cache container
Kafka event streaming container

⚡ Core Functionalities

Recipe CRUD operations
Advanced filtering and search
Image upload and management
User profile management
Real-time notifications
Recipe price point tracking
Response caching
Rate limiting

🚀 Getting Started
Prerequisites
Copy- Python 3.8+
- Docker
- Docker Compose
Installation

Clone the repository

bashCopygit clone https://github.com/yourusername/recipe-api.git
cd recipe-api

Build and run with Docker Compose

bashCopydocker-compose up --build

Access the API

CopyAPI will be available at http://localhost:8000
📝 API Documentation
API endpoints are documented using drf-spectacular. Access the interactive documentation at:
Copyhttp://localhost:8000/api/docs/

🧪 Running Tests
bashCopydocker-compose run --rm app sh -c "python manage.py test"
