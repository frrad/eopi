class MaxQueue:

    def __init__(self):
        self.data = []

    def enqueue(self, toadd):
        self.data.append(toadd)

    def dequeue(self):
        # this is bad, don't do it.
        return self.data.pop(0)

    def max(self):
        return max(self.data)
