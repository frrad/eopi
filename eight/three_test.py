import unittest
import three_fred


class TestEightThree(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ("([]){()}", True),
            ("[()[]{()()}]", True),
            ("{)", False),
            ("[()[]{()()", False),
        ]

    def execute_test(self, name, impl):
        for (x, ans) in self.testcases:
            self.assertEqual(
                impl(x), ans, "%s failed on %s" % (name, x)
            )

    def test_fred(self):
        self.execute_test('fred solution', three_fred.ans)


if __name__ == '__main__':
    unittest.main()
