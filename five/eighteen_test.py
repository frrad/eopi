import eighteen
import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            [
                [
                    [1, 2],
                    [3, 4],
                ],
                [1, 2, 4, 3],
            ],
            [
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16],
                ],
                [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
            ],
        ]

    def execute_test(self, name, impl):
        for inpt, output in self.testcases:
            message = 'Error in "' + name + '" implememntation. Expected output ' + \
                str(output) + ' with input ' + \
                str(inpt) + '. Got ' + str(impl(inpt))
            self.assertEqual(impl(inpt), output, message)

    def test_wrong(self):
        self.execute_test('wrong', eighteen.wrong)

    def test_wronger(self):
        self.execute_test('wronger', eighteen.wronger)
        
    def test_right(self):
        self.execute_test('right', eighteen.spiralize)


if __name__ == '__main__':
    unittest.main()
