from pydantic import BaseModel, Field
from typing import Optional

from rv_form_prefill.models.person import Mother, Father, Child
from rv_form_prefill.models.residence import Residence


class Family(BaseModel):
    residence: Residence
    mother: Mother
    father: Father
    child1: Optional[Child] = Field(default=None)
    child2: Optional[Child] = Field(default=None)
