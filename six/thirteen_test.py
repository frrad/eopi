import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (8, 'gbisn', 'gshgiuregbisnreipngseproingseonvdk;nfvdklldksfl'),
        ]

    def execute_test(self, name, impl):
        for start_ind, sub_str, main_str in self.testcases:
            self.assertEqual(impl(main_str, sub_str), start_ind)


if __name__ == '__main__':
    unittest.main()
