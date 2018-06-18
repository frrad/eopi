import seven_ans
import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ('123', ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']),
            ('27',
             ['AP', 'AQ', 'AR', 'AS', 'BP', 'BQ',
              'BR', 'BS', 'CP', 'CQ', 'CR', 'CS']),
        ]

    def execute_test(self, name, impl):
        for str_orig, str_rev in self.testcases:
            self.assertEqual(set(impl(str_orig)), set(str_rev))
            self.assertEqual(len(impl(str_orig)), len(str_rev))

    def test_nieoh(self):
        self.execute_test('stephanie solution', seven_ans.nieoh_num_to_char)


if __name__ == '__main__':
    unittest.main()
