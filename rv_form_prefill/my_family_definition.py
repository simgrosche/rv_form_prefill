from rv_form_prefill.models.family import Family
from rv_form_prefill.models.person import Mother, Father, Child
from rv_form_prefill.models.residence import Residence


def get_my_family_definition() -> Family:
    residence = Residence(
        street="Main Street",
        street_number="1",
        plz="12345",
        city="Berlin",
        country="Deutschland",
    )
    mother = Mother(
        first_name="Erika",
        last_name="Musterfrau",
        birth_name="Musterfrau",
        birth_date="01.01.1990",
        birth_city="Berlin-Spandau",
        birth_country="DeutschlandMother",
        rentenversicherungsnummer="12345678",
    )
    father = Father(
        first_name="Max",
        last_name="Musterfrau",
        birth_name="Mustermann",
        birth_date="12.12.1991",
        birth_city="Potsdam",
        birth_country="DeutschlandFather",
        rentenversicherungsnummer="9876543",
    )
    child1 = Child(
        first_name="Tim",
        last_name="Musterkind",
        birth_date="01.05.2020",
        birth_city="Berlin1",
        birth_country="Deutschland1",
    )
    child2 = Child(
        first_name="Tom",
        last_name="Musterkind2",
        birth_date="03.06.2020",
        birth_city="Berlin2",
        birth_country="Deutschland2",
    )

    return Family(residence, mother, father, child1, child2)
