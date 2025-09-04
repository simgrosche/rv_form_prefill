import yaml
from pathlib import Path
from rv_form_prefill.models.family import Family
from rv_form_prefill.models.person import Mother, Father, Child
from rv_form_prefill.models.residence import Residence


def get_my_family_definition() -> Family:
    yaml_path = Path(__file__).parent.parent / "family_definition.yaml"
    with open(yaml_path, "r", encoding="utf-8") as f:
        family_data = yaml.safe_load(f)["family"]

    residence = Residence(**family_data["residence"])
    mother = Mother(**family_data["mother"])
    father = Father(**family_data["father"])

    # Get up to 2 children
    children_data = family_data["children"][:2]
    child1 = Child(**children_data[0]) if len(children_data) > 0 else None
    child2 = Child(**children_data[1]) if len(children_data) > 1 else None

    return Family(
        residence=residence, mother=mother, father=father, child1=child1, child2=child2
    )
