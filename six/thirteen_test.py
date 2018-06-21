import thirteen
import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            (8, 'gbisn', 'gshgiuregbisnreipngseproingseonvdk;nfvdklldksfl'),
        ]

    def execute_test(self, name, impl):
        for start_ind, sub_str, main_str in self.testcases:
            self.assertEqual(impl(main_str, sub_str), start_ind)

    def test_right1(self):
        self.execute_test('righ1', thirteen.find_substring_start_ind_simple)

    def test_right2(self):
        self.execute_test('right2', thirteen.find_substring_start_ind_set)

    def test_right3(self):
        self.execute_test(
            'right3', thirteen.find_substring_start_ind_rabin_karp)


if __name__ == '__main__':
    unittest.main()
