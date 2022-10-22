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

def findLastValue(head):
	temp = head

	if (temp == None or temp.next == None):
		return -1

	while (temp != None):

		if (temp.next == None):
			return temp.data
		temp = temp.next

if __name__ == '__main__':
    list1 = UnorderedList()
    head = None
 
    list1.add(4)
    list1.add(9)
    list1.add(5)
    list1.add(1)
    list1.add(7)
    list1.add(3)
    list1.add(8)
    print(findLastValue(list1.head))
