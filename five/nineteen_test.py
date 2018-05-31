import nineteen
import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            [
                [
                    [1, 2],
                    [3, 4],
                ],
                [
                    [3, 1],
                    [4, 2],
                ],
            ],
            [
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16],
                ],
                [
                    [13, 9, 5, 1],
                    [14, 10, 6, 2],
                    [15, 11, 7, 3],
                    [16, 12, 8, 4],
                ],
            ],
        ]

    def execute_test(self, name, impl):
        for inpt, output in self.testcases:
            message = 'Error in "' + name + '" implememntation. Expected output ' + \
                str(output) + ' with input ' + \
                str(inpt) + '. Got ' + str(impl(inpt))
            self.assertEqual(impl(inpt), output, message)

    def test_wrong(self):
        self.execute_test('wrong', nineteen.wrong)

    def test_wronger(self):
        self.execute_test('wronger', nineteen.wronger)


if __name__ == '__main__':
    unittest.main()
