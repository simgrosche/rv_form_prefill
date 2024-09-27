from dataclasses import dataclass, fields


@dataclass(frozen=True)
class FormNames:
    v0800_form: str = "V0800.pdf"
    v0805_form: str = "V0805.pdf"
    v0820_form: str = "V0820.pdf"

    @staticmethod
    def get_all_forms():
        return [getattr(FormNames, field.name) for field in fields(FormNames)]
