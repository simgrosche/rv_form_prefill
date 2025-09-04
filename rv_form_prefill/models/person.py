from pydantic import BaseModel, field_validator
import re


class Person(BaseModel):
    first_name: str
    last_name: str
    birth_city: str
    birth_country: str
    birth_date: str  # "DD.MM.YYYY" or "DDMMYYYY"

    @field_validator("birth_date")
    def validate_birth_date(cls, value):
        # Remove dots and validate format
        cleaned = value.replace(".", "")
        if not re.match(r"^\d{8}$", cleaned):
            raise ValueError("Birth date must be DD.MM.YYYY or DDMMYYYY format")
        return cleaned


class Mother(Person):
    rentenversicherungsnummer: str
    birth_name: str


class Father(Person):
    rentenversicherungsnummer: str
    birth_name: str


class Child(Person):
    pass
