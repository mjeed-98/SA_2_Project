from sqlalchemy.orm import Session
from app.models import SkillService, PortfolioItem
from app.schemas import (
    SkillServiceCreate,
    SkillServiceUpdate,
    PortfolioItemCreate,
    PortfolioItemUpdate
)

# SkillService CRUD Operations
def get_skill_service(db: Session, service_id: int):
    """Get a skill service by ID"""
    return db.query(SkillService).filter(SkillService.serviceId == service_id).first()

def get_all_skill_services(db: Session, skip: int = 0, limit: int = 100):
    """Get all skill services"""
    return db.query(SkillService).offset(skip).limit(limit).all()

def get_services_by_provider(db: Session, provider_id: int, skip: int = 0, limit: int = 100):
    """Get all services for a specific provider"""
    return db.query(SkillService).filter(SkillService.providerId == provider_id).offset(skip).limit(limit).all()

def create_skill_service(db: Session, service: SkillServiceCreate):
    """Create a new skill service"""
    db_service = SkillService(
        providerId=service.providerId,
        title=service.title,
        description=service.description,
        category=service.category,
        price=service.price,
        deliveryTime=service.deliveryTime,
        serviceImageUrl=service.serviceImageUrl,
        isAvailable=service.isAvailable,
        isApproved=service.isApproved
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def update_skill_service(db: Session, service_id: int, service_update: SkillServiceUpdate):
    """Update an existing skill service"""
    db_service = db.query(SkillService).filter(SkillService.serviceId == service_id).first()
    if not db_service:
        return None
    
    update_data = service_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_service, field, value)
    
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def delete_skill_service(db: Session, service_id: int):
    """Delete a skill service"""
    db_service = db.query(SkillService).filter(SkillService.serviceId == service_id).first()
    if not db_service:
        return False
    
    db.delete(db_service)
    db.commit()
    return True

# PortfolioItem CRUD Operations
def get_portfolio_item(db: Session, portfolio_item_id: int):
    """Get a portfolio item by ID"""
    return db.query(PortfolioItem).filter(PortfolioItem.portfolioItemId == portfolio_item_id).first()

def get_portfolio_by_provider(db: Session, provider_id: int, skip: int = 0, limit: int = 100):
    """Get all portfolio items for a specific provider"""
    return db.query(PortfolioItem).filter(PortfolioItem.providerId == provider_id).offset(skip).limit(limit).all()

def create_portfolio_item(db: Session, item: PortfolioItemCreate):
    """Create a new portfolio item"""
    db_item = PortfolioItem(
        providerId=item.providerId,
        projectTitle=item.projectTitle,
        projectDescription=item.projectDescription,
        projectImageUrl=item.projectImageUrl,
        projectLink=item.projectLink
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_portfolio_item(db: Session, portfolio_item_id: int, item_update: PortfolioItemUpdate):
    """Update an existing portfolio item"""
    db_item = db.query(PortfolioItem).filter(PortfolioItem.portfolioItemId == portfolio_item_id).first()
    if not db_item:
        return None
    
    update_data = item_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_portfolio_item(db: Session, portfolio_item_id: int):
    """Delete a portfolio item"""
    db_item = db.query(PortfolioItem).filter(PortfolioItem.portfolioItemId == portfolio_item_id).first()
    if not db_item:
        return False
    
    db.delete(db_item)
    db.commit()
    return True
