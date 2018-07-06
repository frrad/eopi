import unittest
import one_fred
import one_nieoh
import one_david

class TestTenOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            [[8231], [82244]],
            [[1, 2, 3, 8], [2, 2, 4, 4, 8], [0, 1, 4, 4, 6]],
        ]

        self.solns = [
            ('fred solution', one_fred.sort),
            ('steph solution', one_nieoh.merge_sorted)
            ('david solution', one_david.get_union),
        ]

    def test_all(self):
        for name1, sol1 in self.solns:
            for name2, sol2 in self.solns:
                for case in self.testcases:
                    message = 'Expected %s and %s to agree on %s. Got %s and %s.' % (
                        name1, name2, case, sol1(case), sol2(case))
                    self.assertEqual(
                        sol1(case), sol2(case), message
                    )

if __name__ == '__main__':
    unittest.main()
