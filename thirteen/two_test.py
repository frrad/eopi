import unittest
import two_nieoh


class TestThirteenTwo(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([1, 2, 3, 'x', 'x'], [4, 5]),
        ]

        self.solns = [
            ('placeholder solution', lambda a,
             b:list(sorted([x for x in a if x != 'x'] + b))),
            ('nieoh solution', two_nieoh.merge)
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
