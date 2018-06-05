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

    def test_wrong(self):
        self.execute_test(
            'fred solution', lambda x: ' '.join(reversed(x.split(' '))))

if __name__ == '__main__':
    unittest.main()
