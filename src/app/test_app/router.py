from fastapi import APIRouter
from .TestController import test_controller

router = APIRouter(prefix="/test-mod")

@router.get("/test")
async def test():
    return await test_controller.greet_message()
