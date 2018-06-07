
class LinkedList():

    def __init__(self, data):
        if len(data) == 0:
            return None
        self.value = data[0]
        self.next = None
        if len(data) > 1:
            self.next = LinkedList(data[1:])

    def __str__(self):
        ans = str(self.value)
        if self.next is not None:
            ans += "->" + str(self.next)
        return ans

    def as_list(self):
        ans = [self.value]
        if self.next is not None:
            ans += self.next.as_list()
        return ans
