from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints
StudentIdStr=Annotated[str,StringConstraints(pattern=r"^ST[A-Z]{2}\d{4}$")]
DescriptionStr=Annotated[str,StringConstraints(min_length=5, max_length=100)]

class UserCreate(BaseModel):
    student_id:StudentIdStr
    description:DescriptionStr
    priority:int=Field(ge=1,le=5)
    equipment_id:int=Field(gt=0)

class UserRead(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:int
    student_id:StudentIdStr
    description:DescriptionStr
    priority:int
    equipment_id:int
    status:str
