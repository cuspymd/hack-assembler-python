import os
from hack_assembler.parser import Parser
from hack_assembler.instruction import InstructionType
from hack_assembler.code import Code


def run(input_path: str):
    folder_path, file_name = os.path.split(input_path)
    file_base_name, _ = os.path.splitext(file_name)
    output_path = os.path.join(folder_path, f"{file_base_name}.hack")

    with open(input_path, "r") as file:
        input_text = file.read()

    with open(output_path, "w") as file:
        parser = Parser(input_text)
        code = Code()

        while parser.has_more_lines():
            parser.advance()

            match parser.instructionType():
                case InstructionType.A_INSTRUCTION:
                    symbol = parser.symbol()
                    binary = bin(int(symbol))[2:].zfill(16)
                    file.write(f"{binary}\n")

                case InstructionType.C_INSTRUCTION:
                    comp = parser.comp()
                    comp = code.comp(comp)
                    dest = parser.dest()
                    dest = code.dest(dest)
                    jump = parser.jump()
                    jump = code.jump(jump)
                    file.write(f"111{comp}{dest}{jump}\n")
