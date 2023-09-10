
from typing import List

from hack_assembler.instruction import Instruction, InstructionType


class Parser:
    def __init__(self, file_text: str):
        self.lines = self._get_valid_lines(file_text)
        self.current_line_number = -1
        self.current_instruction: Instruction = None

    def _get_valid_lines(self, file_text: str) -> List[str]:
        return [
            valid_text
            for line in file_text.splitlines()
            if (valid_text := self._get_valid_text(line))
        ]

    def _get_valid_text(self, text: str) -> str:
        strip_text = text.strip()
        COMMENT_ID = "//"
        if COMMENT_ID in strip_text:
            return strip_text.split(COMMENT_ID)[0]
        else:
            return strip_text

    def has_more_lines(self):
        return self.current_line_number < len(self.lines)-1

    def advance(self):
        self.current_line_number += 1
        self.current_instruction = Instruction(self.lines[self.current_line_number])

    def instructionType(self) -> InstructionType:
        return self.current_instruction.instruction_type
