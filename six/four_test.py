import four
import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.testcases = [
            (['a','b','a','c','_'], 4, ['d', 'd', 'd', 'd', 'c']),
        ]
    
    def execute_test(self, name, impl):
        for arr_orig, size, arr_replace in self.testcases:
            self.assertEqual(impl(arr_orig, size), arr_replace)
    
    def test_right1(self):
        self.execute_test('right1', four.replace_and_remove)
        