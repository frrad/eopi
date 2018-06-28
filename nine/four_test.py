import unittest
import four_fred
import test_helper


class TestNineFour(unittest.TestCase):

    def setUp(self):
        temp = [test_helper.ex_pptree(i) for i in xrange(100)]
        self.testcases = [(test_helper.rand_leaf(
            x, 0), test_helper.rand_leaf(x, 1)) for x in temp]

        self.solns = [
            ('fred solution', four_fred.lca),
        ]

    def test_all(self):
        for name1, sol1 in self.solns:
            for name2, sol2 in self.solns:
                for (a, b) in self.testcases:
                    message = 'expected %s and %s to agree on %s, %s' % (
                        name1, name2, a, b)
                    self.assertEqual(
                        sol1(a, b), sol2(a, b), message
                    )

if __name__ == '__main__':
    unittest.main()
