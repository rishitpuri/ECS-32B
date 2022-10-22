class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.No = 0

    def slice(self, start, stop):
        if (start < 1) or (start > stop) or (stop > self.No + 1):
            print ("Invalid")
            return None
        stop = stop - 1
        present = self.head
        c = 1
        while present is not None:
            if c == start:
                break
            present = present.next
            c += 1
        n = Node(present.data)
        front = n
        back = front
        while c < stop:
            present = present.next
            n = Node(present.data)
            back.next = n
            back = back.next
            c += 1
        return front