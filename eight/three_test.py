import three_david
import unittest


class TestSevenOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ('{ab[()c}', False),
            ('{ab[(', False),
            ('{ab[()]c}', True),
        ]

    def execute_test(self, name, impl):
        for test_str, valid_parens in self.testcases:
            self.assertEqual(impl(test_str), valid_parens)

    def test_david(self):
        self.execute_test('david solution', three_david.check_parens)


if __name__ == '__main__':
    unittest.main()
