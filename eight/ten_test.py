import unittest
import ten_fred


class TestEightTen(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (
                [4, 3, 4, 9, 3],
                ['e', 'e', 'd', 'e', 'e', 'e', 'd', 'd', 'd'],
                [4, 4, (4, 3), 4, 9, 9, (3, 9), (4, 9), (9, 3)],
            ),
        ]

    def execute_test(self, name, impl):
        for data, ops, answers in self.testcases:
            x = impl()
            dataPtr = 0
            for (i, (op, ans)) in enumerate(zip(ops, answers)):
                if op == 'e':
                    x.enqueue(data[dataPtr])
                    dataPtr += 1
                    self.assertEqual(
                        x.max(), ans
                    )
                if op == 'd':
                    out = x.dequeue()
                    self.assertEqual(
                        out, ans[0]
                    )
                    self.assertEqual(
                        x.max(), ans[1]
                    )

    def test_fred(self):
        self.execute_test('fred solution', ten_fred.MaxQueue)


if __name__ == '__main__':
    unittest.main()
