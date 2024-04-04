from fastapi import APIRouter

from .test_app.router import router as test_routes 

AppRouter = APIRouter()

AppRouter.include_router(test_routes)