import unittest
import one_fred
import one_nieoh


class TestThirteenOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (list('112467789'), list('12333')),
        ]

        self.solns = [
            ('placeholder solution', one_fred.hack),
            ('nieoh solution', one_nieoh.intersect)
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
