from rv_form_prefill.models.family import Family
from rv_form_prefill.models.fill_tasks import FillTask


class FillDictHandler:
    def __init__(self, my_family: Family):
        self.my_family = my_family

    def get_fill_dict(self, fill_task: FillTask):
        if fill_task == FillTask.V0800_fill_as_mother:
            return {
                "PAF_VSNR_trim": self.my_family.mother.rentenversicherungsnummer,
                "Q_PAF_Vers_Vorname": self.my_family.mother.first_name,
                "Q_PAF_Vers_Name": self.my_family.mother.last_name,
                "Q_PAF_Vers_GebName": self.my_family.mother.birth_name,
                "Q_PAF_Vers_GebOrt": self.my_family.mother.birth_city,
                "Q_PAF_Vers_GebDat_trim": self.my_family.mother.birth_date,
                "ET_VERSNR": self.my_family.father.rentenversicherungsnummer,
                "ET_VN": self.my_family.father.first_name,
                "ET_Name": self.my_family.father.last_name,
                "ET_GN": self.my_family.father.birth_name,
                "ET_GD": self.my_family.father.birth_date,
                "Q_PAF_Vers_Straße_Postfach": f"{self.my_family.residence.street} {self.my_family.residence.street_number}",
                "Q_PAF_Vers_PLZ": self.my_family.residence.plz,
                "Q_PAF_Vers_Wohnort": self.my_family.residence.city,
                "Q_PAF_Vers_Land": self.my_family.residence.country,
                "KD_Name_1": f"{self.my_family.child1.last_name}, {self.my_family.child1.first_name}",
                "DAT_KD_Geb_1": self.my_family.child1.birth_date,
                "KD_GebOrt_1": self.my_family.child1.birth_city,
                "KD_GebStaat_1": self.my_family.child1.birth_country,
                "KD_Name_2": f"{self.my_family.child2.last_name}, {self.my_family.child2.first_name}",
                "DAT_KD_Geb_2": self.my_family.child2.birth_date,
                "KD_GebOrt_2": self.my_family.child2.birth_city,
                "KD_GebStaat_2": self.my_family.child2.birth_country,
            }
        elif fill_task == FillTask.V0800_fill_as_father:
            return {
                "PAF_VSNR_trim": self.my_family.father.rentenversicherungsnummer,
                "Q_PAF_Vers_Vorname": self.my_family.father.first_name,
                "Q_PAF_Vers_Name": self.my_family.father.last_name,
                "Q_PAF_Vers_GebName": self.my_family.father.birth_name,
                "Q_PAF_Vers_GebOrt": self.my_family.father.birth_city,
                "Q_PAF_Vers_GebDat_trim": self.my_family.father.birth_date,
                "ET_VERSNR": self.my_family.mother.rentenversicherungsnummer,
                "ET_VN": self.my_family.mother.first_name,
                "ET_Name": self.my_family.mother.last_name,
                "ET_GN": self.my_family.mother.birth_name,
                "ET_GD": self.my_family.mother.birth_date,
                "Q_PAF_Vers_Straße_Postfach": f"{self.my_family.residence.street} {self.my_family.residence.street_number}",
                "Q_PAF_Vers_PLZ": self.my_family.residence.plz,
                "Q_PAF_Vers_Wohnort": self.my_family.residence.city,
                "Q_PAF_Vers_Land": self.my_family.residence.country,
                "KD_Name_1": f"{self.my_family.child1.last_name}, {self.my_family.child1.first_name}",
                "DAT_KD_Geb_1": self.my_family.child1.birth_date,
                "KD_GebOrt_1": self.my_family.child1.birth_city,
                "KD_GebStaat_1": self.my_family.child1.birth_country,
                "KD_Name_2": f"{self.my_family.child2.last_name}, {self.my_family.child2.first_name}",
                "DAT_KD_Geb_2": self.my_family.child2.birth_date,
                "KD_GebOrt_2": self.my_family.child2.birth_city,
                "KD_GebStaat_2": self.my_family.child2.birth_country,
            }
        elif fill_task in [
            FillTask.V0805_fill_as_mother_child1,
            FillTask.V0805_fill_as_mother_child2,
            FillTask.V0805_fill_as_father_child1,
            FillTask.V0805_fill_as_father_child2,
        ]:
            if fill_task in [
                FillTask.V0805_fill_as_mother_child1,
                FillTask.V0805_fill_as_mother_child2,
            ]:
                parent_filldict = {
                    "PAF_VSNR_trim": self.my_family.mother.rentenversicherungsnummer,
                    "VERS_VN": self.my_family.mother.first_name,
                    "VERS_N": self.my_family.mother.last_name,
                    "VERS_GN": self.my_family.mother.birth_name,
                    "VERS_ERZIEH_VSNR1_1": self.my_family.father.rentenversicherungsnummer,
                    "ELTERNTEIL_VN_1": self.my_family.father.first_name,
                    "ELTERNTEIL_N_1": self.my_family.father.last_name,
                    "ELTERNTEIL_GN_1": self.my_family.father.birth_name,
                    "ELTERNTEIL_GDAT_1": self.my_family.father.birth_date,
                }
            elif fill_task in [
                FillTask.V0805_fill_as_father_child1,
                FillTask.V0805_fill_as_father_child2,
            ]:
                parent_filldict = {
                    "PAF_VSNR_trim": self.my_family.father.rentenversicherungsnummer,
                    "VERS_VN": self.my_family.father.first_name,
                    "VERS_N": self.my_family.father.last_name,
                    "VERS_GN": self.my_family.father.birth_name,
                    "VERS_ERZIEH_VSNR1_1": self.my_family.mother.rentenversicherungsnummer,
                    "ELTERNTEIL_VN_1": self.my_family.mother.first_name,
                    "ELTERNTEIL_N_1": self.my_family.mother.last_name,
                    "ELTERNTEIL_GN_1": self.my_family.mother.birth_name,
                    "ELTERNTEIL_GDAT_1": self.my_family.mother.birth_date,
                }
            else:
                raise NotImplementedError("Case not implemented, check implementation")
            if fill_task in [
                FillTask.V0805_fill_as_mother_child1,
                FillTask.V0805_fill_as_father_child1,
            ]:
                child_filldict = {
                    "KIND_VN_1": self.my_family.child1.first_name,
                    "KIND_N_1": self.my_family.child1.last_name,
                    "KIND_GDAT_1": self.my_family.child1.birth_date,
                }
            elif fill_task in [
                FillTask.V0805_fill_as_mother_child2,
                FillTask.V0805_fill_as_father_child2,
            ]:
                child_filldict = {
                    "KIND_VN_1": self.my_family.child2.first_name,
                    "KIND_N_1": self.my_family.child2.last_name,
                    "KIND_GDAT_1": self.my_family.child2.birth_date,
                }
            else:
                raise NotImplementedError("Case not implemented, check implementation")
            return {**parent_filldict, **child_filldict}
        elif fill_task in [
            FillTask.V0820_together_child1,
            FillTask.V0820_together_child2,
        ]:
            parent_filldict = {
                "ZIFFER_1_1_VSNR1": self.my_family.mother.rentenversicherungsnummer,
                "MUTTER_VN_1": self.my_family.mother.first_name,
                "MUTTER_N_1": self.my_family.mother.last_name,
                "MUTTER_GN_1": self.my_family.mother.birth_name,
                "MUTTER_GDAT_1": self.my_family.mother.birth_date,
                "MUTTER_GO_1": f"{self.my_family.mother.birth_city}, {self.my_family.mother.birth_country}",
                "MUTTER_ADR_1": f"{self.my_family.residence.street} {self.my_family.residence.street_number}",
                "MUTTER_PLZ_1": self.my_family.residence.plz,
                "MUTTER_ORT_1": self.my_family.residence.city,
                "ZIFFER_1_2_VSNR1": self.my_family.father.rentenversicherungsnummer,
                "VATER_VN_1": self.my_family.father.first_name,
                "VATER_N_1": self.my_family.father.last_name,
                "VATER_GN_1": self.my_family.father.birth_name,
                "VATER_GDAT_1": self.my_family.father.birth_date,
                "VATER_GO_1": f"{self.my_family.father.birth_city}, {self.my_family.father.birth_country}",
                "VATER_ADR_1": f"{self.my_family.residence.street} {self.my_family.residence.street_number}",
                "VATER_PLZ_1": self.my_family.residence.plz,
                "VATER_ORT_1": self.my_family.residence.city,
            }
            if fill_task in [FillTask.V0820_together_child1]:
                child_filldict = {
                    "KIND_N_V_1": f"{self.my_family.child1.last_name}, {self.my_family.child1.first_name}",
                    "KIND_GDAT_1": self.my_family.child1.birth_date,
                }
            elif fill_task in [FillTask.V0820_together_child2]:
                child_filldict = {
                    "KIND_N_V_1": f"{self.my_family.child2.last_name}, {self.my_family.child2.first_name}",
                    "KIND_GDAT_1": self.my_family.child2.birth_date,
                }
            else:
                raise NotImplementedError("Case not implemented, check implementation")
            return {**parent_filldict, **child_filldict}
        else:
            raise NotImplementedError(
                f"Fill dict for task {fill_task} was not implemented."
            )
