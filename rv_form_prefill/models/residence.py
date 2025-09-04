from pydantic import BaseModel, field_validator



class Residence(BaseModel):
    street: str
    street_number: str
    plz: str
    city: str
    country: str

    @field_validator("plz")
    def validate_plz(cls, value):
        if not value.isdigit():
            raise ValueError("PLZ must be numeric")
        return value


