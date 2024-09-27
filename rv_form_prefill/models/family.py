from dataclasses import dataclass

from rv_form_prefill.models.person import Mother, Father, Child
from rv_form_prefill.models.residence import Residence


@dataclass
class Family:
    residence: Residence
    mother: Mother
    father: Father
    child1: Child
    child2: Child
