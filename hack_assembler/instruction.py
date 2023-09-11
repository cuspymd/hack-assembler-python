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

    @property
    def symbol(self) -> str:
        match self.instruction_type:
            case InstructionType.A_INSTRUCTION:
                return self.text[1:]
            case InstructionType.L_INSTRUCTION:
                return self.text[1:-1]
            case _:
                return ""

    @property
    def dest(self) -> str:
        return words[0] if len(words := self.text.split("=")) > 1 else ""

    @property
    def comp(self) -> str:
        if len(words := self.text.split("=")) > 1:
            valid_text = words[1]
        else:
            valid_text = self.text

        if len(words := valid_text.split(";")) > 1:
            return words[0]
        else:
            return valid_text

    @property
    def jump(self) -> str:
        return words[1] if len(words := self.text.split(";")) > 1 else ""
