import six
import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ('Bob likes Alice', 'Alice likes Bob'),
            ('the quick brown fox jumps over the lazy dog',
             'dog lazy the over jumps fox brown quick the'),
        ]

    def execute_test(self, name, impl):
        for str_orig, str_rev in self.testcases:
            self.assertEqual(impl(str_orig), str_rev)

    def test_fred(self):
        self.execute_test(
            'fred solution', lambda x: ' '.join(reversed(x.split(' '))))

    def test_fred2(self):
        self.execute_test('fred solution 2', six.troll)

    def test_nieoh(self):
        self.execute_test('stephanie solution', six.six_nieoh)

if __name__ == '__main__':
    unittest.main()
