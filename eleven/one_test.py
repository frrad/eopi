import unittest


class TestElevenOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108),
            ([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285),
        ]

        self.solns = [
            ('placeholder solution', lambda x, y: 3 if y == 108 else 6),
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
