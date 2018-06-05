import six
import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.testcases = [
            ('Bob likes Alice', 'Alice likes Bob'),
        ]
    
    def execute_test(self, name, impl):
        for str_orig, str_rev in self.testcases:
            self.assertEqual(impl(str_orig), str_rev)
    
    def test_right1(self):
        self.execute_test('right1', six.reverse_words_simple)
        
    def test_right2(self):
        self.execute_test('right2', six.reverse_words_prealloc)

        
if __name__ == '__main__':
    unittest.main()