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
