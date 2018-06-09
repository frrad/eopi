import linked_list
import one_fred
import unittest


class TestSevenOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (([1, 2, 4, 7], [1, 4, 4, 5]),
             [1, 1, 2, 4, 4, 4, 5, 7]),
        ]

    def execute_test(self, name, impl):
        for (x, y), merged in self.testcases:
            self.assertEqual(
                impl(linked_list.LinkedList(x),
                     linked_list.LinkedList(y)).as_list(),
                merged,
            )

    def test_fred(self):
        self.execute_test('fred solution', one_fred.merge_lists)

if __name__ == '__main__':
    unittest.main()
