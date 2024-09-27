from rv_form_prefill.form_handler.form_fill_dict import FillDictHandler
from rv_form_prefill.form_handler.form_names import FormNames
from rv_form_prefill.models.fill_tasks import FillTask
from rv_form_prefill.my_family_definition import get_my_family_definition
from rv_form_prefill.util.util import run_fill_task, download_and_preprocess_rv_forms

if __name__ == "__main__":
    download_and_preprocess_rv_forms(download=True, verify_hash=True)

    my_family = get_my_family_definition()
    fill_dict_handler = FillDictHandler(my_family)

    form_name = FormNames.v0800_form
    for fill_task in [FillTask.V0800_fill_as_mother, FillTask.V0800_fill_as_father]:
        run_fill_task(fill_dict_handler, fill_task, form_name)

    form_name = FormNames.v0805_form
    for fill_task in [
        FillTask.V0805_fill_as_mother_child1,
        FillTask.V0805_fill_as_mother_child2,
        FillTask.V0805_fill_as_father_child1,
        FillTask.V0805_fill_as_father_child2,
    ]:
        run_fill_task(fill_dict_handler, fill_task, form_name)

    form_name = FormNames.v0820_form
    for fill_task in [FillTask.V0820_together_child1, FillTask.V0820_together_child2]:
        run_fill_task(fill_dict_handler, fill_task, form_name)
