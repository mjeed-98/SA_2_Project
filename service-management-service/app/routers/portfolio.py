from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import PortfolioItemCreate, PortfolioItemResponse, PortfolioItemUpdate
from app import crud

router = APIRouter(prefix="/api/portfolio", tags=["portfolio"])

@router.post("", response_model=PortfolioItemResponse, status_code=status.HTTP_201_CREATED)
def create_portfolio_item(item: PortfolioItemCreate, db: Session = Depends(get_db)):
    """Create a new portfolio item"""
    return crud.create_portfolio_item(db, item)

@router.get("/provider/{providerId}", response_model=list[PortfolioItemResponse])
def get_provider_portfolio(providerId: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all portfolio items for a specific provider"""
    portfolio_items = crud.get_portfolio_by_provider(db, providerId, skip=skip, limit=limit)
    return portfolio_items

@router.put("/{portfolioItemId}", response_model=PortfolioItemResponse)
def update_portfolio_item(portfolioItemId: int, item_update: PortfolioItemUpdate, db: Session = Depends(get_db)):
    """Update an existing portfolio item"""
    portfolio_item = crud.update_portfolio_item(db, portfolioItemId, item_update)
    if not portfolio_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Portfolio item with ID {portfolioItemId} not found"
        )
    return portfolio_item

@router.delete("/{portfolioItemId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_portfolio_item(portfolioItemId: int, db: Session = Depends(get_db)):
    """Delete a portfolio item"""
    success = crud.delete_portfolio_item(db, portfolioItemId)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Portfolio item with ID {portfolioItemId} not found"
        )
    return None
