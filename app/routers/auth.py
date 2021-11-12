from fastapi import status, Response, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app import models, schemas, utils, database, oauth2


router = APIRouter(tags=['Authentication'])


@router.post("/login", status_code = status.HTTP_200_OK, response_model=schemas.Token)
def login(user_creds: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_creds.username).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = f"invalid credentials"
        )

    if not utils.verify(user_creds.password, user.password):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = f"invalid credentials"
        )

    access_token = oauth2.create_access_token(data={
        "user_id": user.id
    })
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"user with id {id} was not found"
        )
    return user
