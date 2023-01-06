import os
import sys
import unittest

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
sys.path.append(current_path)

from query_doc_matching import QueryDocMatchingPromptware  # noqa


class TestQueryDocMatchingPromptware(unittest.TestCase):
    def test_write_to_directory(self):
        software = QueryDocMatchingPromptware()
        file_path = software.info.write_to_directory(current_path)
        self.assertTrue(os.path.exists(file_path))
