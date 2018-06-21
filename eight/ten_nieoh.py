from collections import deque

class MaxQueue:
    def __init__(self):
        self.queue = deque('')
        self.max_candidates = deque('')

    def enqueue(self, data):
        self.queue.append(data)
        while len(self.max_candidates) > 0 and data > self.max_candidates[-1]:
            self.max_candidates.pop()
        self.max_candidates.append(data)

    def dequeue(self):
        deq = self.queue.popleft()
        if deq == self.max_candidates[0]:
            self.max_candidates.popleft()
        return deq

    def max(self):
        if len(self.max_candidates) > 0:
            return self.max_candidates[0]
        return ''
