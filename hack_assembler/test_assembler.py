import unittest
import os
import hack_assembler.assembler as assembler


class TestAssembler(unittest.TestCase):
    def test_assembler_given_no_symbol(self):
        self._test_assembler("./test_data/RectL.asm")
        self._test_assembler("./test_data/Add.asm")
        self._test_assembler("./test_data/MaxL.asm")

    def _test_assembler(self, input_path: str):
        folder_path, file_name = os.path.split(input_path)
        file_base_name, _ = os.path.splitext(file_name)

        OUT_FILE = os.path.join(folder_path, f"{file_base_name}.hack")
        SOLUTION_FILE = os.path.join(folder_path, f"Solution_{file_base_name}.hack")
        if os.path.exists(OUT_FILE):
            os.remove(OUT_FILE)

        assembler.run(input_path)
        self.assertTrue(os.path.exists(OUT_FILE))

        with open(SOLUTION_FILE, 'r') as solution_file:
            solution_text = solution_file.read()

        with open(OUT_FILE, 'r') as file:
            output_text = file.read()

        self.assertEqual(output_text, solution_text)
        os.remove(OUT_FILE)
