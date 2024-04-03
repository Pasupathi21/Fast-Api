from fastapi import APIRouter
from .TestController import test_controller

router = APIRouter()

@router.get("/test")
async def test():
    return test_controller.greet_message()