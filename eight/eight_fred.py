import collections


class Queue:

    def __init__(self, capacity=0):
        self.data = collections.deque()
        self.num_stored = 0

    def enqueue(self, item):
        self.num_stored += 1
        self.data.append(item)

    def dequeue(self):
        self.num_stored -= 1
        return self.data.popleft()

    def num_elts(self):
        return self.num_stored
