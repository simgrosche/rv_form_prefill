from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    birth_city: str
    birth_country: str
    birth_date: str  # "DD.MM.YYYY" (or "DDMMYYYY")

    def __post_init__(self):
        self.birth_date = self.birth_date.replace(".", "")


@dataclass
class Mother(Person):
    rentenversicherungsnummer: str
    birth_name: str


@dataclass
class Father(Person):
    rentenversicherungsnummer: str
    birth_name: str


@dataclass
class Child(Person):
    pass
