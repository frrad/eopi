import unittest


class TestTwelveOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ("the quick brown fox jumps over the lazy dog", "asdfqwerty"),
            ("thequickbrownfoxjumpsoverthelazydog", "test a      d   f"),
        ]

        self.solns = [
            ('placeholder solution', lambda mag, let: True),
        ]

    def test_all(self):
        for name1, sol1 in self.solns:
            for name2, sol2 in self.solns:
                for case in self.testcases:
                    message = 'Expected %s and %s to agree on %s. Got %s and %s.' % (
                        name1, name2, case, sol1(*case), sol2(*case))
                    self.assertEqual(
                        sol1(*case), sol2(*case), message
                    )

if __name__ == '__main__':
    unittest.main()
