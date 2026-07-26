from enum import Enum
from pydantic import BaseModel


class UserRole(str, Enum):
    researcher = "researcher"
    laboratory_specialist = "laboratory_specialist"
    healthcare_institution = "healthcare_institution"
    student = "student"


class SampleCreate(BaseModel):
    sample_id: str
    organism: str
    tissue: str
    notes: str | None = None


class UserCreate(BaseModel):
    name: str
    email: str
    role: UserRole