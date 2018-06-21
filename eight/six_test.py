import unittest
import six_fred
import six_nieoh

class TestEightSix(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([4, 3, 4, 9, 3, 5, 5, 0, 7, 3, 9, 3, 5, 6, 9], [9]),
            ([6, 8, 3, 2, 8, 0, 7, 5, 7, 3], [8, 7, 3]),
            ([0, 7, 2, 9, 0, 6, 0, 2], [9, 6, 2]),
            ([3, 4, 8, 9, 1], [9, 1]),
            ([1, 2, 3, 4], [4]),
            ([4, 3, 2, 1], [4, 3, 2, 1]),
            ([], []),
        ]

    def execute_test(self, name, impl):
        for (data, soln) in self.testcases:
            message = "%s failed on input %s. Got %s but wanted %s." % (
                name, data, impl(data), soln)
            self.assertEqual(impl(data), soln, message)

    def test_fred(self):
        self.execute_test('fred solution', six_fred.sunset)

    def test_nieoh1(self):
        self.execute_test('nieoh solution1', six_nieoh.sunset_view)

    def test_nieoh2(self):
        self.execute_test('nieoh solution with maxqueue', six_nieoh.sunset_view_maxq)

if __name__ == '__main__':
    unittest.main()
