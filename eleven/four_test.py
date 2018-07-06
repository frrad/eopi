import unittest


class TestElevenOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            16, 300
        ]

        self.solns = [
            ('placeholder solution', lambda x: 4 if x == 16 else 17),
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
