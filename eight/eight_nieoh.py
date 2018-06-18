class CircularQueue:

    def __init__(self, n):
        self.len = n
        self.size = 0
        self.circular_queue = [0] * n
        self.start = 0
        self.end = 0

    def enqueue(self, data):
        self.size += 1
        print self.size
        if self.size > self.len:
            self.resize(self.len)
        print self.end
        self.circular_queue[self.end] = data
        self.end = (self.end + 1)%self.len
        print self.end, self.circular_queue

    def dequeue(self):
        deq = self.circular_queue[self.start]
        self.size -= 1
        self.start = (self.start + 1)%self.len
        print 'dequing', deq
        print self.start, self.circular_queue
        return deq

    def num_elts(self):
        return self.size
   
    def resize(self, num):
        temp = [0] * num
        timp = self.start
        for i in range(self.len):
            temp[i] = self.circular_queue[timp % self.len]
            timp += 1
        self.circular_queue = temp + [0] * num
        self.start = 0
        self.end = self.len
        self.len = 2 * num
