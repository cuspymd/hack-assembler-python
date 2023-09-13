import os
import sys
from hack_assembler.parser import Parser
from hack_assembler.instruction import InstructionType
from hack_assembler.code import Code
from hack_assembler.symbol_table import SymbolTable


class Assembler:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.empty_symbol_address = 16

    def run(self, input_path: str):
        folder_path, file_name = os.path.split(input_path)
        file_base_name, _ = os.path.splitext(file_name)
        output_path = os.path.join(folder_path, f"{file_base_name}.hack")

        with open(input_path, "r") as file:
            input_text = file.read()

        with open(output_path, "w") as out_file:
            self._run_phase_one(input_text)
            self._run_phase_two(input_text, out_file)

    def _run_phase_one(self, input_text: str):
        line_num = 0
        parser = Parser(input_text)

        while parser.has_more_lines():
            parser.advance()
            if parser.instructionType() == InstructionType.L_INSTRUCTION:
                symbol = parser.symbol()
                self.symbol_table.add_entry(symbol, line_num)
            else:
                line_num += 1

    def _run_phase_two(self, input_text: str, out_file):
        parser = Parser(input_text)
        code = Code()

        while parser.has_more_lines():
            parser.advance()

            match parser.instructionType():
                case InstructionType.A_INSTRUCTION:
                    symbol = parser.symbol()
                    binary = self._process_symbol(symbol)
                    out_file.write(f"{binary}\n")

                case InstructionType.C_INSTRUCTION:
                    comp = parser.comp()
                    comp = code.comp(comp)
                    dest = parser.dest()
                    dest = code.dest(dest)
                    jump = parser.jump()
                    jump = code.jump(jump)
                    out_file.write(f"111{comp}{dest}{jump}\n")

    def _process_symbol(self, symbol: str) -> str:
        if not symbol.isdigit():
            if self.symbol_table.contains(symbol):
                symbol = self.symbol_table.get_address(symbol)
            else:
                self.symbol_table.add_entry(symbol, self.empty_symbol_address)
                symbol = self.empty_symbol_address
                self.empty_symbol_address += 1

        return bin(int(symbol))[2:].zfill(16)


if __name__ == "__main__":
    print(f"Start assembling for '{sys.argv[1]}'")
    Assembler().run(sys.argv[1])
    print("Completed")
