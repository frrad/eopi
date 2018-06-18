import eight_david
import unittest


class TestEightEight(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (5, [5, 7, 4, 3, 3, 2], 2, [44, 6], [6, 44, 2, 3, 3, 4]),
        ]

    def execute_test(self, name, impl):
        for init_cap, enq1, num_deq1, enq2, ans in self.testcases:
            q = impl(init_cap)
            for val in enq1:
                q.enqueue(val)
            for i in range(num_deq1):
                q.dequeue()
            for val in enq2:
                q.enqueue(val)
            self.assertEqual(q.to_list(), ans)

    def test_david(self):
        self.execute_test('david solution', eight_david.CircularQueue1)


if __name__ == '__main__':
    unittest.main()
