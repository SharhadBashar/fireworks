from pydantic import BaseModel

from typing import Optional

class Identity(BaseModel):
    surname: str
    given_name: str
    sex: str
    date_of_birth: str
    date_of_issue: str
    date_of_expiry: str
    nationality: Optional[str] = None
    place_of_birth: Optional[str] = None
    passport_number: Optional[str] = None
    height: Optional[str] = None
    eye_color: Optional[str] = None
    hair_color: Optional[str] = None
    license_number: Optional[str] = None
    address: Optional[str] = None

class Passport(BaseModel):
    surname: str
    given_name: str
    sex: str
    nationality: str
    date_of_birth: str
    place_of_birth: str
    passport_number: str
    date_of_issue: str
    date_of_expiry: str

class License(BaseModel):
    surname: str
    given_name: str
    sex: str
    date_of_birth: str
    height: str
    eye_color: str
    hair_color: str
    license_number: str
    date_of_issue: str
    date_of_expiry: str
    address: str
