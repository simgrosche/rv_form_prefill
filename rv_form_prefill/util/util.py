import re
import subprocess
from copy import copy
from pathlib import Path

from rv_form_prefill.form_handler.file_downloader import (
    FileDownloader,
    get_fn_raw_form_data,
)
from rv_form_prefill.form_handler.form_fill_dict import FillDictHandler
from rv_form_prefill.form_handler.form_names import FormNames
from rv_form_prefill.models.fill_tasks import FillTask
from rv_form_prefill.util.paths import (
    URL_BASE,
    URL_POSTFIX,
    FORMS_PATH,
    FORMS_OUTPUT_PATH,
)


def download_and_preprocess_rv_forms(download=True, verify_hash=True):
    for rv_form in FormNames.get_all_forms():
        downloader = FileDownloader(
            URL_BASE + rv_form + URL_POSTFIX, FORMS_PATH / rv_form
        )
        if download:
            downloader.download()
        if verify_hash:
            downloader.verify_md5_hash()
        downloader.extract_fdf_form_data()


def get_form_keys(fn_form_data: Path) -> list[str]:
    pattern = "/T \((.*)\)"

    with open(fn_form_data, "r", encoding="ISO-8859-1") as file:
        content = file.read()

    results = re.findall(pattern, content)

    return results


def _get_value_of_key(fn_form_data: Path, key: str) -> str | None:
    pattern = f"/T \({key}\)\n/V \((.*)\)"

    with open(fn_form_data, "r", encoding="ISO-8859-1") as file:
        content = file.read()

    results = re.findall(pattern, content)
    if len(results) == 0:
        return None
    elif len(results) == 1:
        return results[0]
    else:
        raise ValueError("Found multiple entries for single form key")


def validate_fill_dict_matches_form_fields(form_name: str, fill_dict: dict[str, str]):
    fn_form = FORMS_PATH / form_name
    fn_form_data = get_fn_raw_form_data(fn_form)

    form_keys = get_form_keys(fn_form_data)
    print(f"All form keys detected:\n{form_keys}")

    form_key_values_provided = get_already_provided_key_value_pairs(
        fn_form_data, form_keys
    )
    if len(form_key_values_provided) > 0:
        print(form_key_values_provided)

    keys_not_in_form = set(fill_dict.keys()).difference(set(form_keys))

    if len(keys_not_in_form) > 0:
        raise ValueError(
            f"There are form keys provided in dict that are not present in form.\n{keys_not_in_form}"
        )


def get_already_provided_key_value_pairs(fn_form_data, form_keys):
    form_key_values_provided = {}
    for form_key in form_keys:
        value = _get_value_of_key(fn_form_data, form_key)
        if value:
            form_key_values_provided[form_key] = value
    return form_key_values_provided


def fill_form(form_name: str, fill_task: FillTask, fill_dict: dict[str, str]):
    fn_form = FORMS_PATH / form_name
    fn_form_data = get_fn_raw_form_data(fn_form)

    with open(fn_form_data, "r", encoding="ISO-8859-1") as file:
        data = file.read()
    new_data = copy(data)
    for replace_pattern in fill_dict.keys():
        new_data = new_data.replace(
            f"/T ({replace_pattern})\n/V ()",
            f"/T ({replace_pattern})\n/V ({fill_dict[replace_pattern]})",
        )

    # Open the file in write mode to overwrite it with new content
    with open(
        FORMS_OUTPUT_PATH / f"{fill_task.name}.fdf", "w", encoding="ISO-8859-1"
    ) as file:
        file.write(new_data)
    subprocess.call(
        [
            "pdftk",
            str(fn_form),
            "fill_form",
            str(FORMS_OUTPUT_PATH / f"{fill_task.name}.fdf"),
            "output",
            str(FORMS_OUTPUT_PATH / f"{fill_task.name}.pdf"),
        ]
    )
    subprocess.call(["rm", str(FORMS_OUTPUT_PATH / f"{fill_task.name}.fdf")])


def run_fill_task(
    fill_dict_handler: FillDictHandler,
    fill_task: FillTask,
    form_name: str,
):
    print(fill_task.name)
    fill_dict = fill_dict_handler.get_fill_dict(fill_task)
    validate_fill_dict_matches_form_fields(form_name, fill_dict)
    fill_form(form_name, fill_task, fill_dict)
