from fastapi import APIRouter

from .ProfileController import profile_controller

from ..model.profile import Profile 

router = APIRouter(prefix="/profile")

@router.post("/create")
async def create_profile(payload: Profile):
    # return payload
    print("router payload", payload)
    formatted = {
            "ful_name": payload.full_name,
            "mobile_no": payload.mobile_no,
            "address": payload.address,
            "skill": payload.skill,
            "gender": payload.gender,
            "optional": payload.optional
    }
    return profile_controller.crated_profile(formatted)
