import unittest
import one_fred


class TestEightOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            [4, 3, 4, 9, 3, 5, 5, 0, 7, 3, 9, 3, 5, 6, 9]
        ]

    def execute_test(self, name, impl):
        for data in self.testcases:
            x = impl()
            for i, datum in enumerate(data):
                x.push(datum)
                self.assertEqual(
                    x.max(), max(data[:i + 1])
                )
            for i in xrange(len(data) - 1):
                x.pop()
                self.assertEqual(
                    x.max(), max(data[:-i - 1])
                )

    def test_fred(self):
        self.execute_test('fred solution', one_fred.MaxStack)


if __name__ == '__main__':
    unittest.main()
