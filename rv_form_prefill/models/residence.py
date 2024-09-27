from dataclasses import dataclass


@dataclass
class Residence:
    street: str
    street_number: str
    plz: str
    city: str
    country: str
