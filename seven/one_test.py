import linked_list
import one_david
import unittest


class TestSevenThree(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (linked_list.LinkedList([1, 2, 3, 8, 29, 1000]), 
             linked_list.LinkedList([4, 18, 19, 72, 80, 99]), 
             [1, 2, 3, 4, 8, 18, 19, 29, 72, 80, 99, 1000]),
        ]

    def execute_test(self, name, impl):
        for A, B, merged in self.testcases:
            self.assertEqual(impl(A, B).as_list(), merged)

    def test_david(self):
        self.execute_test('david solution', one_david.merge_lists)


if __name__ == '__main__':
    unittest.main()
