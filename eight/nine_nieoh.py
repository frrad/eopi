
class PancakeQueue:
    """Implement a queue using stacks"""

    def __init__(self):
        self.enque = []
        self.deque = []
        self.head = self.deque[-1] if self.deque else ''
        self.tail = self.enque[-1] if self.enque else ''
        
    def enqueue(self, data):
        self.enque.append(data)

    def dequeue(self):
        if not self.deque and not self.enque:
            return ''
        if not self.deque:
            while self.enque:
                self.deque.append(self.enque.pop())
        deq = self.deque.pop()
        return deq



