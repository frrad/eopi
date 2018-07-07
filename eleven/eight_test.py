import unittest
import eight_fred


class TestElevenEight(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([3, 2, 1, 5, 4], 1),
            ([3, 2, 1, 5, 4], 3),
            ([3, 2, 1, 5, 4], 5),
        ]

        self.solns = [
            ('fred solution', eight_fred.kth_largest),
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
