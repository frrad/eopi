import linked_list
import six_david
import unittest


class TestSevenThree(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (linked_list.LinkedList([1, 41, 4, 15, 5, 7]), 3, [1, 41, 15, 5, 7]),
        ]

    def execute_test(self, name, impl):
        for ll, delete_node_depth, ans in self.testcases:
            delete_node = ll
            for i in range(delete_node_depth-1):
                delete_node = delete_node.next
            impl(delete_node)
            self.assertEqual(ll.as_list(), ans)

    def test_david(self):
        self.execute_test('david solution', six_david.delete_node)


if __name__ == '__main__':
    unittest.main()