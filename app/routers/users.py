from fastapi import status, Response, HTTPException, Depends, APIRouter

from sqlalchemy.orm import Session

from app import models, schemas, utils, database


router = APIRouter(prefix='/users', tags=['Users'])


@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user_data: schemas.UserCreate, db: Session = Depends(database.get_db)):
    user_data.password = utils.hash(user_data.password)
    user = models.User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"user with id {id} was not found"
        )
    return user
