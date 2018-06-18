import unittest
import eight_fred


class TestEightEight(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            [4, 3, 4, 9, 3, 5, 5, 0, 7, 3, 9, 3, 5, 6, 9]
        ]

    def execute_test(self, name, impl):
        for data in self.testcases:
            q = impl(2)
            for i, datum in enumerate(data):
                q.enqueue(datum)
                self.assertEqual(
                    q.num_elts(), i + 1
                )
            for i in xrange(len(data)):
                self.assertEqual(
                    q.dequeue(), data[i]
                )
                self.assertEqual(
                    q.num_elts(), len(data) - i - 1
                )

    def test_fred(self):
        self.execute_test('fred solution', eight_fred.Queue)


if __name__ == '__main__':
    unittest.main()
