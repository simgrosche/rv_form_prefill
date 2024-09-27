from enum import Enum


class FillTask(Enum):
    V0800_fill_as_mother = "V0800_fill_as_mother"
    V0800_fill_as_father = "V0800_fill_as_father"
    V0805_fill_as_mother_child1 = "V0805_fill_as_mother_child1"
    V0805_fill_as_mother_child2 = "V0805_fill_as_mother_child2"
    V0805_fill_as_father_child1 = "V0805_fill_as_father_child1"
    V0805_fill_as_father_child2 = "V0805_fill_as_father_child2"
    V0820_together_child1 = "V0820_together_child1"
    V0820_together_child2 = "V0820_together_child2"
