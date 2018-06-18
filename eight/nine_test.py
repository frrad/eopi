import unittest
import eight_fred  # re-use


class TestEightNine(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            [4, 3, 4, 9, 3, 5, 5, 0, 7, 3, 9, 3, 5, 6, 9]
        ]

    def execute_test(self, name, impl):
        for data in self.testcases:
            q = impl()
            for i, datum in enumerate(data):
                q.enqueue(datum)
            for i in xrange(len(data)):
                self.assertEqual(
                    q.dequeue(), data[i]
                )

    def test_fred(self):
        self.execute_test('fred solution', eight_fred.Queue)


if __name__ == '__main__':
    unittest.main()
