from fastapi import APIRouter

router = APIRouter(prefix="/animes")


@router.get("/")
def get_animes():
    pass
