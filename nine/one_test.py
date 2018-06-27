import unittest
import one_fred
import test_helper


class TestNineOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            test_helper.ex_tree(i) for i in xrange(100)
        ]

        self.solns = [
            ('fred solution', one_fred.height_balanced),
        ]

    def test_all(self):
        for name1, sol1 in self.solns:
            for name2, sol2 in self.solns:
                for case in self.testcases:
                    message = 'expected %s and %s to agree on %s' % (
                        name1, name2, case)
                    self.assertEqual(
                        sol1(case), sol2(case), message
                    )

if __name__ == '__main__':
    unittest.main()
