import yaml
from pathlib import Path
from rv_form_prefill.models.family import Family
from rv_form_prefill.models.person import Mother, Father, Child
from rv_form_prefill.models.residence import Residence


def get_my_family_definition() -> Family:
    yaml_path = Path(__file__).parent.parent / 'family_definition.yaml'
    with open(yaml_path) as f:
        data = yaml.safe_load(f)['family']
    
    residence = Residence(**data['residence'])
    mother = Mother(**data['mother'])
    father = Father(**data['father'])
    children = [Child(**child_data) for child_data in data['children']]
    
    return Family(residence, mother, father, *children)


