from fastapi import APIRouter

router = APIRouter(prefix="/chapters")


@router.get("/")
def get_chapters():
    pass
