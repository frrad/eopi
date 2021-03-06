import linked_list
import seven_fred
import seven_nieoh
import unittest


class TestSevenSeven(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([1, 2, 4, 7], 2),
            ([1, 2, 4, 7], 1),
            ([2, 3, 7, 9, 34, 5, 5], 3),
        ]

    def execute_test(self, name, impl):
        for l, k in self.testcases:
            x = linked_list.LinkedList(l)
            fucking = impl(x, k)

            self.assertEqual(
                fucking.as_list(), l[:-k] + l[len(l)- k +1:]
            )

    def test_fred(self):
        self.execute_test('fred solution', seven_fred.delete_minus_k)

    def test_nieoh(self):
        self.execute_test('nieoh solution', seven_nieoh.delete_last_k)
    

if __name__ == '__main__':
    unittest.main()
