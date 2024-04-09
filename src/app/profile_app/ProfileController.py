from ..db.database import DB
from ..model.profile import Profile
from fastapi.encoders import jsonable_encoder


class ProfileController:

    def __init__(self):
        pass
        
    async def crated_profile(self, payload):
        print('crated_profile >>>>> ', payload)
        # formatted = {
        #     "ful_name": payload.full_name,
        #     "mobile_no": payload.mobile_no,
        #     "address": payload.address,
        #     "skill": payload.skill,
        #     "gender": payload.gender,
        #     "optional": payload.optional
        # }
        
        print("formatted payload >>>>>>", payload)
        profile_res = DB.profile.insert_one(payload)
        return profile_res

profile_controller = ProfileController()

