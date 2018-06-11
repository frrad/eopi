import linked_list
import eight_fred
import unittest


class TestSevenEight(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (linked_list.LinkedList([1, 4, 4, 5, 5, 7]), [1, 4, 5, 7]),
            (linked_list.LinkedList([1, 4, 4, 5, 5, 5, 7]), [1, 4, 5, 7]),
        ]

    def execute_test(self, name, impl):
        for ll, deduped in self.testcases:
            impl(ll)
            self.assertEqual(ll.as_list(), deduped)

    def test_david(self):
        self.execute_test('fred solution', eight_fred.remove_duplicates)


if __name__ == '__main__':
    unittest.main()
