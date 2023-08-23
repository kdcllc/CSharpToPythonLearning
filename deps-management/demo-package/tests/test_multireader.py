import unittest

import demo_reader.multirader

class TestMultireader(unittest.TestCase):
    def test_initialization(self):
        demo_reader.multirader.MultiReader("test_file.txt")