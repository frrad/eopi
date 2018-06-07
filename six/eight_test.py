import eight_fred
import unittest


class TestSixEight(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (1, "1"),
            (2, "11"),
            (7, "13112221"),
        ]

    def execute_test(self, name, impl):
        for str_orig, str_rev in self.testcases:
            self.assertEqual(impl(str_orig), str_rev)

    def test_fred(self):
        self.execute_test('fred solution', eight_fred.look_and_say)

if __name__ == '__main__':
    unittest.main()
