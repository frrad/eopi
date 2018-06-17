import six_david
import unittest


class TestSevenOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([5, 7, 4, 3, 3, 2], [7, 4, 3, 2]),
        ]

    def execute_test(self, name, impl):
        for heights, view_heights in self.testcases:
            self.assertEqual(impl(heights), view_heights)

    def test_david(self):
        self.execute_test('david solution', six_david.get_sunset_view_buildings)


if __name__ == '__main__':
    unittest.main()
