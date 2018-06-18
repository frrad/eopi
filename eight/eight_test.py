import unittest
import eight_fred
import eight_nieoh

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

            # Checks for enqing and deqing same number of stuff
            q = impl(2)
            datum = data[0]
            q.enqueue(datum)
            q.enqueue(datum)
            q.dequeue()
            self.assertEqual(
                q.dequeue(), datum
            )
            self.assertEqual(
                q.num_elts(), 0
            )

            # Want to check circularity enq * 3 + deq * 2
            # Then check size but seems to break /shrug
            q = impl(2)
            for i, datum in enumerate(data):
                q.enqueue(datum)
                q.enqueue(datum)
                q.enqueue(datum)
                q.dequeue()
                self.assertEqual(
                    q.dequeue(), datum
                )
                self.assertEqual(
                    q.num_elts(), i+1
                )


    def test_fred(self):
        self.execute_test('fred solution', eight_fred.Queue)

    def test_nieoh(self):
        self.execute_test('nieoh solution', eight_nieoh.CircularQueue)


if __name__ == '__main__':
    unittest.main()
