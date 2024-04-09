from fastapi import APIRouter

from .test_app.router import router as test_routes 
from .profile_app.router import router as profile_routes

AppRouter = APIRouter()

AppRouter.include_router(test_routes)
AppRouter.include_router(profile_routes)