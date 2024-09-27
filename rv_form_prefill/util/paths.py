from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.resolve()

FORMS_PATH = PROJECT_ROOT / "forms"
FORMS_OUTPUT_PATH = PROJECT_ROOT / "forms_output"


URL_BASE = "https://www.deutsche-rentenversicherung.de/SharedDocs/Formulare/DE/_pdf/"
URL_POSTFIX = "?__blob=publicationFile"
