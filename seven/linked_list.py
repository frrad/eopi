class LinkedList():

    def __init__(self, data):
        if len(data) == 0:
            return None

        self.value = data[0]
        self.next = None

        if len(data) > 2:
            self.next = LinkedList(data[1:])

    def __str__(self):
        ans = str(self.value)
        if self.next is not None:
            ans += "->" + str(self.next)

        return ans
