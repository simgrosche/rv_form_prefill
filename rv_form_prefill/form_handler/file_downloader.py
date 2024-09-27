import logging
import subprocess
from pathlib import Path

import requests
from typing import Union

from rv_form_prefill.util.md5_hash import generate_md5

FDF_EXTENSION = "form_data.fdf"


class FileDownloader:
    def __init__(self, url: str, filename: Path, set_new_md5_hash: bool = False):
        self._url: str = url
        self._filename: Path = filename
        self._set_new_md5_hash = set_new_md5_hash

    def download(self) -> Union[bool, None]:
        try:
            response = requests.get(self._url, stream=True)
            if response.status_code == 200:
                with open(self._filename, "wb") as f:
                    f.write(response.content)
                logging.warning(f"Wrote file to {self._filename}")
                return True
            else:
                return False
        except requests.RequestException as e:
            print(f"Error downloading file: {e}")
            return None

    def verify_md5_hash(self):
        file_md5 = generate_md5(self._filename)
        if self._set_new_md5_hash:
            with open(
                self._filename.parent / (self._filename.name + ".md5hash"), "w"
            ) as f:
                f.write(file_md5)

        with open(self._filename.parent / (self._filename.name + ".md5hash"), "r") as f:
            file_md5_expected = f.read()
        if file_md5_expected != file_md5:
            raise ValueError(
                f"MD5 hash does not match.\nGot {file_md5}\nExpected: {file_md5_expected}"
            )

    @property
    def _fn_form_data(self):
        return get_fn_raw_form_data(self._filename)

    def extract_fdf_form_data(self):
        subprocess.call(
            [
                "pdftk",
                str(self._filename),
                "generate_fdf",
                "output",
                str(self._fn_form_data),
            ]
        )


def get_fn_raw_form_data(fn_form: Path):
    return fn_form.parent / (fn_form.name + FDF_EXTENSION)
