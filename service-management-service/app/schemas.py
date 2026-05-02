from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

# SkillService Schemas
class SkillServiceBase(BaseModel):
    providerId: int
    title: str = Field(..., min_length=1, description="Service title cannot be empty")
    description: Optional[str] = None
    category: Optional[str] = None
    price: float = Field(..., ge=0, description="Price must be >= 0")
    deliveryTime: Optional[int] = None
    serviceImageUrl: Optional[str] = None
    isAvailable: bool = True
    isApproved: bool = False

    @validator('title')
    def title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()

class SkillServiceCreate(SkillServiceBase):
    pass

class SkillServiceUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(None, ge=0)
    deliveryTime: Optional[int] = None
    serviceImageUrl: Optional[str] = None
    isAvailable: Optional[bool] = None
    isApproved: Optional[bool] = None

    @validator('title')
    def title_not_empty(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('Title cannot be empty')
        return v.strip() if v else None

class SkillServiceResponse(SkillServiceBase):
    serviceId: int
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

# PortfolioItem Schemas
class PortfolioItemBase(BaseModel):
    providerId: int
    projectTitle: str = Field(..., min_length=1, description="Project title cannot be empty")
    projectDescription: Optional[str] = None
    projectImageUrl: Optional[str] = None
    projectLink: Optional[str] = None

    @validator('projectTitle')
    def project_title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Project title cannot be empty')
        return v.strip()

class PortfolioItemCreate(PortfolioItemBase):
    pass

class PortfolioItemUpdate(BaseModel):
    projectTitle: Optional[str] = None
    projectDescription: Optional[str] = None
    projectImageUrl: Optional[str] = None
    projectLink: Optional[str] = None

    @validator('projectTitle')
    def project_title_not_empty(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('Project title cannot be empty')
        return v.strip() if v else None

class PortfolioItemResponse(PortfolioItemBase):
    portfolioItemId: int
    createdAt: datetime

    class Config:
        from_attributes = True
