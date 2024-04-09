from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"
    others = "others"

class Skill(BaseModel):
    skill: str
    level: float

class Profile(BaseModel):
    full_name: str
    mobile_no: int
    address: str
    skill: List[Skill]
    gender: Gender
    optional: Optional[bool] = None




# def single_value(param):
#     return param


# def multi_values(params):
#     return [ single_value(param) for param in params]
