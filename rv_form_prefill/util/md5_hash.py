import hashlib
from pathlib import Path


def generate_md5(file_path: Path | str) -> str:
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        hash_md5.update(f.read())
    return hash_md5.hexdigest()
