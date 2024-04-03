from fastapi import APIRouter
from app import main as Main

router = APIRouter()

@router.get("/test/2")
async def test():
    return Main.test_controller.greet_message()


