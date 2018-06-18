import one_david
import unittest


class TestEightOne(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([5,4,7,3,7], 2, 7),
            ([5,4,7,3,7], 3, 5),
        ]

    def execute_test(self, name, impl):
        for vals, num_pop, max_val in self.testcases:
            stack = impl()
            for val in vals:
                stack.push(val)
            for i in range(num_pop):
                stack.pop()
            self.assertEqual(stack.max(), max_val)

    def test_david1(self):
        self.execute_test('david solution 1', one_david.MaxStack1)
        
    def test_david2(self):
        self.execute_test('david solution 2', one_david.MaxStack2)
        
    def test_david3(self):
        self.execute_test('david solution 3', one_david.MaxStack3)

if __name__ == '__main__':
    unittest.main()
