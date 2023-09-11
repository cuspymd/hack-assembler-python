import unittest
from hack_assembler.instruction import InstructionType

from hack_assembler.parser import Parser


class TestParser(unittest.TestCase):
    def test_has_more_lines_given_one_line(self):
        parser = Parser("@01")
        self.assertTrue(parser.has_more_lines())

    def test_has_more_lines_given_empty_line(self):
        parser = Parser("")
        self.assertFalse(parser.has_more_lines())

        parser = Parser("\n   \n     \n")
        self.assertFalse(parser.has_more_lines())

        parser = Parser("\n   \n     @R1\n")
        self.assertTrue(parser.has_more_lines())

    def test_has_more_lines_given_comment_line(self):
        parser = Parser("// comment")
        self.assertFalse(parser.has_more_lines())

    def test_advance(self):
        parser = Parser("@R0")
        self.assertTrue(parser.has_more_lines())
        parser.advance()
        self.assertFalse(parser.has_more_lines())

    def test_advance_given_two_lines(self):
        parser = Parser("@R0\nD=M")
        self.assertTrue(parser.has_more_lines())
        parser.advance()
        self.assertTrue(parser.has_more_lines())
        parser.advance()
        self.assertFalse(parser.has_more_lines())

    def test_instructionType(self):
        parser = Parser("@01")
        parser.advance()
        self.assertEqual(parser.instructionType(), InstructionType.A_INSTRUCTION)

    def test_instructionType_given_c_instruction(self):
        parser = Parser("M=1")
        parser.advance()
        self.assertEqual(parser.instructionType(), InstructionType.C_INSTRUCTION)

    def test_instructionType_given_l_instruction(self):
        parser = Parser("(LOOP)")
        parser.advance()
        self.assertEqual(parser.instructionType(), InstructionType.L_INSTRUCTION)

    def test_symbol_given_a_instruction(self):
        parser = Parser("@01")
        parser.advance()
        self.assertEqual(parser.symbol(), "01")

    def test_symbol_given_l_instruction(self):
        parser = Parser("(LOOP)")
        parser.advance()
        self.assertEqual(parser.symbol(), "LOOP")

    def test_c_instruction_given_dest(self):
        parser = Parser("M=1")
        parser.advance()
        self.assertEqual(parser.dest(), "M")
        self.assertEqual(parser.comp(), "1")
        self.assertEqual(parser.jump(), "")

    def test_c_instruction_given_JMP(self):
        parser = Parser("0;JMP")
        parser.advance()
        self.assertEqual(parser.dest(), "")
        self.assertEqual(parser.comp(), "0")
        self.assertEqual(parser.jump(), "JMP")

    def test_c_instruction_given_comp(self):
        parser = Parser("D+1")
        parser.advance()
        self.assertEqual(parser.dest(), "")
        self.assertEqual(parser.comp(), "D+1")
        self.assertEqual(parser.jump(), "")

    def test_c_instruction_given_all(self):
        parser = Parser("ADM=D+1;JGT")
        parser.advance()
        self.assertEqual(parser.dest(), "ADM")
        self.assertEqual(parser.comp(), "D+1")
        self.assertEqual(parser.jump(), "JGT")
