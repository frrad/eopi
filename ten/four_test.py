import unittest
import four_fred


class TestTenFour(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([(4, 5, 4), (1, 2, 1), (1, 2, 3),
              (3, 2, 1), (4, 5, 6)], 3),
        ]

        self.solns = [
            ('fred solution', four_fred.nearest_stars),
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
