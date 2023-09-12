import unittest
import os
import hack_assembler.assembler as assembler


class TestAssembler(unittest.TestCase):
    def test_assembler_given_no_symbol(self):
        OUT_FILE = "./test_data/RectL.hack"
        SOLUTION_FILE = "./test_data/SolutionL.hack"
        if os.path.exists(OUT_FILE):
            os.remove(OUT_FILE)

        assembler.run("./test_data/RectL.asm")
        self.assertTrue(os.path.exists(OUT_FILE))

        with open(SOLUTION_FILE, 'r') as solution_file:
            solution_text = solution_file.read()

        with open(OUT_FILE, 'r') as file:
            output_text = file.read()

        self.assertEqual(output_text, solution_text)
