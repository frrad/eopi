import linked_list
import three_fred
import three_david
import three_nieoh
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
        
    def test_david1(self):
        self.execute_test('david naive solution', three_david.find_cycle_naive)
        
    def test_david2(self):
        self.execute_test('david inplace solution', three_david.find_cycle_inplace)
    def test_nieoh(self):
        self.execute_test('nieoh solution', three_nieoh.cyclicQ)
if __name__ == '__main__':
    unittest.main()
