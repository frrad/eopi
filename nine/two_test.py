import unittest
import two_fred
import test_helper
import two_nieoh


class TestNineTwo(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            test_helper.ex_tree(i, randvals=True) for i in xrange(1000, 1100)
        ]

        self.solns = [
            ('fred solution', two_fred.symmetric),
            ('nieoh solution', two_nieoh.symmetric)
        ]

    def test_all(self):
        for name1, sol1 in self.solns:
            for name2, sol2 in self.solns:
                for case in self.testcases:
                    message = 'expected %s and %s to agree on %s.' % (
                        name1, name2, case)
                    self.assertEqual(
                        sol1(case), sol2(case), message
                    )

if __name__ == '__main__':
    unittest.main()
