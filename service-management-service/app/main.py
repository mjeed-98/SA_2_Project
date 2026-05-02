from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import services, portfolio

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Service Management API",
    description="API for managing skill services and portfolio items",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(services.router)
app.include_router(portfolio.router)

# Health check endpoint
@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "service-management-service",
        "version": "1.0.0"
    }

@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Service Management API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
