# Recipe API Backend 🍳

 ## *🌟Features *

### Advanced REST API Architecture
Complete CRUD operations using ViewSets
Custom endpoints with APIViews
Complex data modeling with nested serializers

### **Performance Optimization**

Redis caching for frequently accessed recipes
Rate limiting on API endpoints
Response caching using Python decorators

### *Scalable Infrastructure*

Kubernetes container orchestration
Docker containerization
Apache Kafka for real-time event handling

### *Security & Authentication*

Custom user authentication system
Secure user profile management
Protected API endpoints

## *🛠️ Tech Stack *

Backend: Django REST Framework
Database: PostgreSQL
Caching: Redis
Containers: Docker, Docker-Compose, Kubernetes
Message Queue: Apache Kafka
Web Server: Nginx

## *📸 API Documentation Screenshots *
<div align="center">

| API Overview | API Endpoints |
|:---:|:---:|
| <img src="docs/images/WhatsApp Image 2025-01-16 at 01.20.01_902232fc.jpg" alt="API Overview" width="500"/> | <img src="docs/images/WhatsApp Image 2025-01-17 at 23.45.35_c8f7bdd1.jpg" alt="API Endpoints" width="500"/> |
| **API Schemas** | **Authentication Flow** |
| <img src="docs/images/WhatsApp Image 2025-01-17 at 23.46.06_90281d63.jpg" alt="API Schemas" width="500"/> | <img src="docs/images/WhatsApp Image 2025-01-17 at 23.46.36_ca518875.jpg" alt="Authentication" width="500"/> |

</div>

## *🚀 Quick Start*
Prerequisites

Docker & Docker Compose
Setup & Installation

Clone the repository

bashCopygit clone https://github.com/madhavgiga1/recipe-api.git
cd recipe-api


# Start services
docker-compose up

# Create superuser (in a new terminal)

docker-compose exec web python manage.py createsuperuser

## *🧪 Testing *
Run the test suite:

docker-compose run --rm web python manage.py test

# Run specific test file
docker-compose run --rm web python manage.py test app.tests.test_recipes

## *🛠️ Development *

docker-compose run --rm web python manage.py makemigrations

# Apply migrations
docker-compose run --rm web python manage.py migrate

# Collect static files
docker-compose run --rm web python manage.py collectstatic

# Create superuser
docker-compose run --rm web python manage.py createsuperuser

### *📦 Project Structure*
Copyrecipe-api/
├── app/
│   ├── core/          # Core functionality
│   ├── recipe/        # Recipe related features
│   ├── user/          # User management
│   └── tests/         # Test suite
├── docs/              # Documentation
├── requirements/      # Dependencies
└── docker/           # Docker configuration
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
