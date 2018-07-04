import unittest
import three_fred
import three_david


class TestTenThree(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([2, 3, 5, 7, 7, 9], 2),
            ([3, -1, 2, 6, 4, 5, 8], 2),
        ]

        self.solns = [
            ('fred solution', three_fred.sort),
            ('david solution', three_david.sort_almost_sorted),
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
