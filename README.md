# Service Management Service

A FastAPI microservice for managing skill services and portfolio items in the SkillBridge platform.

## Overview

This service provides endpoints to manage:
- **Skill Services**: Services offered by service providers
- **Portfolio Items**: Portfolio projects showcasing provider's work

## Features

- FastAPI with async support
- SQLAlchemy ORM with PostgreSQL
- Pydantic models for data validation
- Docker and Docker Compose support
- CORS middleware enabled
- Health check endpoint
- Comprehensive error handling
- Automatic API documentation (Swagger UI)

## Technology Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Containerization**: Docker & Docker Compose

## Project Structure

```
service-management-service/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app setup
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   └── routers/
│       ├── __init__.py
│       ├── services.py      # Service endpoints
│       └── portfolio.py     # Portfolio endpoints
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```

## API Endpoints

### Health Check
- `GET /health` - Service health status

### Skill Services
- `POST /api/services` - Create a new service
- `GET /api/services` - List all services
- `GET /api/services/{serviceId}` - Get a specific service
- `GET /api/services/provider/{providerId}` - Get services by provider
- `PUT /api/services/{serviceId}` - Update a service
- `DELETE /api/services/{serviceId}` - Delete a service

### Portfolio
- `POST /api/portfolio` - Create a portfolio item
- `GET /api/portfolio/provider/{providerId}` - Get provider's portfolio
- `PUT /api/portfolio/{portfolioItemId}` - Update a portfolio item
- `DELETE /api/portfolio/{portfolioItemId}` - Delete a portfolio item

## Data Models

### SkillService
```json
{
  "serviceId": 1,
  "providerId": 101,
  "title": "Web Development",
  "description": "Full-stack web development services",
  "category": "Development",
  "price": 100.00,
  "deliveryTime": 14,
  "serviceImageUrl": "https://example.com/image.jpg",
  "isAvailable": true,
  "isApproved": true,
  "createdAt": "2024-01-01T00:00:00",
  "updatedAt": "2024-01-01T00:00:00"
}
```

### PortfolioItem
```json
{
  "portfolioItemId": 1,
  "providerId": 101,
  "projectTitle": "E-commerce Platform",
  "projectDescription": "A full-featured e-commerce platform",
  "projectImageUrl": "https://example.com/project.jpg",
  "projectLink": "https://example.com",
  "createdAt": "2024-01-01T00:00:00"
}
```

## Validation Rules

- `title` / `projectTitle`: Cannot be empty
- `price`: Must be >= 0
- `providerId`: Required field
- `isAvailable`: Defaults to `true`
- `isApproved`: Defaults to `false`

## Setup and Installation

### Prerequisites
- Docker and Docker Compose (for containerized setup)
- Python 3.11+ (for local development)
- PostgreSQL 15+ (for local database)

### Docker Setup (Recommended)

1. Clone the repository
2. Navigate to the project directory
3. Run Docker Compose:

```bash
docker-compose up -d
```

The API will be available at `http://localhost:8000`

### Local Development Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
# Unix/macOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database and update `.env` file with connection string

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the service is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost:5432/service_management
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK`: Successful GET request
- `201 Created`: Successful resource creation
- `204 No Content`: Successful deletion
- `400 Bad Request`: Validation error
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

Example error response:
```json
{
  "detail": "Service with ID 999 not found"
}
```

## Running Tests

(Add test commands when tests are created)

## License

This project is part of the SkillBridge platform.
