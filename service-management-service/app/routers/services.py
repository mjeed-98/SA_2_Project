from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import SkillServiceCreate, SkillServiceResponse, SkillServiceUpdate
from app import crud

router = APIRouter(prefix="/api/services", tags=["services"])

@router.post("", response_model=SkillServiceResponse, status_code=status.HTTP_201_CREATED)
def create_service(service: SkillServiceCreate, db: Session = Depends(get_db)):
    """Create a new skill service"""
    return crud.create_skill_service(db, service)

@router.get("", response_model=list[SkillServiceResponse])
def get_all_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all skill services"""
    services = crud.get_all_skill_services(db, skip=skip, limit=limit)
    return services

@router.get("/{serviceId}", response_model=SkillServiceResponse)
def get_service(serviceId: int, db: Session = Depends(get_db)):
    """Get a specific skill service by ID"""
    service = crud.get_skill_service(db, serviceId)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Service with ID {serviceId} not found"
        )
    return service

@router.get("/provider/{providerId}", response_model=list[SkillServiceResponse])
def get_provider_services(providerId: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all services for a specific provider"""
    services = crud.get_services_by_provider(db, providerId, skip=skip, limit=limit)
    return services

@router.put("/{serviceId}", response_model=SkillServiceResponse)
def update_service(serviceId: int, service_update: SkillServiceUpdate, db: Session = Depends(get_db)):
    """Update an existing skill service"""
    service = crud.update_skill_service(db, serviceId, service_update)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Service with ID {serviceId} not found"
        )
    return service

@router.delete("/{serviceId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(serviceId: int, db: Session = Depends(get_db)):
    """Delete a skill service"""
    success = crud.delete_skill_service(db, serviceId)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Service with ID {serviceId} not found"
        )
    return None
