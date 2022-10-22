class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def searchRec(self, list1, item):
         
        if(not list1):
            return False
        if(list1.data == item):
            return True
        return self.searchRec(list1.next, item)

if __name__ == '__main__':
    list1 = UnorderedList()
 
    list1.add(4)
    list1.add(9)
    list1.add(5)
    list1.add(1)
    list1.add(7)
    list1.add(3)
    list1.add(8)

    item = 3 
if list1.searchRec(list1.head,item):
    print("yes")
else:
    print("no")
