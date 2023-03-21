import os
import sys
import unittest

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
sys.path.append(current_path)

from .software import InstructionTaskPromptware  # noqa


class TestInstructionTaskPromptware(unittest.TestCase):
    def test_write_to_directory(self):
        software = InstructionTaskPromptware()
        file_path = software.info.write_to_directory(current_path)
        self.assertTrue(os.path.exists(file_path))
