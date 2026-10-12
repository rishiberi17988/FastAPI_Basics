from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated, Literal, Optional


class PatientCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    date_of_birth: date | None = None
    gender: Annotated[Literal['male', 'female', 'others'] , Field(..., description='Gender of the patient')]
    phone: str = Field(pattern=r"^[0-9]{10}$"  , description= "Must be exactly 10 digits" )


class PatientUpdate(BaseModel):
    first_name: str | None = Field(default=None, min_length=1, max_length=100)
    last_name: str | None = Field(default=None, min_length=1, max_length=100)
    date_of_birth: date | None = None
    gender: str | None = Field(default=None, max_length=30)
    phone: str | None = Field(default=None, max_length=20)


class PatientRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    patient_id: int
    first_name: str
    last_name: str
    date_of_birth: date | None
    gender: str | None
    phone: str | None
    created_at: datetime
