import seven
import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.testcases = [
            ('23', set(['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF'])),
        ]
    
    def execute_test(self, name, impl):
        for digits, mnemonics in self.testcases:
            num_unique = len(mnemonics.symmetric_difference(impl(digits)))
            self.assertEqual(num_unique, 0)
    
    def test_right1(self):
        self.execute_test('right1', seven.get_mnemonics)
        