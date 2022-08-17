from fastapi import APIRouter

from ..models.auth import Login

router = APIRouter()


@router.post("/login")
def login(credentials: Login):
    pass
