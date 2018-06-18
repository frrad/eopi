# An actual working solution, but with bad runtime
class MaxStack:

    def __init__(self):
        self.data = []

    def push(self, datum):
        self.data.append(datum)

    def pop(self):
        return self.data.pop()

    def max(self):
        return max(self.data)
