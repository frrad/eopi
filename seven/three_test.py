import linked_list
import three_fred
import unittest


class TestSevenThree(unittest.TestCase):

    def setUp(self):
        A = linked_list.LinkedList([1, 2, 3])
        B = linked_list.LinkedList([4, 5, 6, 7, 8, 9, 10])
        B.next.next.next.next.next.next.next = B.next.next.next

        self.testcases = [
            (A, None),
            (B, B.next.next.next),
        ]

    def execute_test(self, name, impl):
        for ll, node in self.testcases:
            self.assertEqual(impl(ll), node)

    def test_fred(self):
        self.execute_test('fred solution', three_fred.first_loop)

if __name__ == '__main__':
    unittest.main()
