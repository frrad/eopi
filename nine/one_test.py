import unittest
import one_david
from one_david import BinaryTree


class TestNineOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([5, 6, 3], True),
            ([5, 6, 7, 8, 3], False),
        ]

    def execute_test(self, name, impl):
        for vals, is_balanced in self.testcases:
            btree = BinaryTree()
            for val in vals:
                btree.insert(val)
            self.assertEqual(impl(btree), is_balanced)

    def test_david(self):
        self.execute_test('david solution', one_david.is_height_balanced)


if __name__ == '__main__':
    unittest.main()
