from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

class SkillService(Base):
    __tablename__ = "skill_services"

    serviceId = Column(Integer, primary_key=True, index=True)
    providerId = Column(Integer, nullable=False, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    category = Column(String(100), index=True)
    price = Column(Float, nullable=False)
    deliveryTime = Column(Integer)  # in days
    serviceImageUrl = Column(String(500))
    isAvailable = Column(Boolean, default=True)
    isApproved = Column(Boolean, default=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class PortfolioItem(Base):
    __tablename__ = "portfolio_items"

    portfolioItemId = Column(Integer, primary_key=True, index=True)
    providerId = Column(Integer, nullable=False, index=True)
    projectTitle = Column(String(255), nullable=False, index=True)
    projectDescription = Column(Text)
    projectImageUrl = Column(String(500))
    projectLink = Column(String(500))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
