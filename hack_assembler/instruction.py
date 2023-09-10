from enum import Enum


class InstructionType(Enum):
    A_INSTRUCTION = 1
    C_INSTRUCTION = 2
    L_INSTRUCTION = 3


class Instruction:
    def __init__(self, instruction_text) -> None:
        self.text = instruction_text

    @property
    def instruction_type(self) -> InstructionType:
        instruction_type = InstructionType.C_INSTRUCTION
        if self.text[0] == "@":
            instruction_type = InstructionType.A_INSTRUCTION
        elif self.text[0] == "(":
            instruction_type = InstructionType.L_INSTRUCTION

        return instruction_type
