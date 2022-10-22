class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def Slice(point):
 
        Length = length(point)
        if Length < 2:
 
            staring = point
            stop = None
            return starting, stop
 
        pre = point
 
        hopCount = (length - 1) // 2 
        for i in range(hopCount):
            pre = pre.next

            starting = point
            stop = pre.next
            pre.next = None
 
        return staring, stop