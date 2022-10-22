class Node :
	def __init__(self, data) :
		self.data = data
		self.next = None
		self.prev = None
	
class Deque2 :
	def __init__(self) :
		self.frt = None
		self.Rear = None
		self.decSize = 0
	
	def isEmpty(self) :
		if (self.decSize == 0) :
			return True
		else :
			return False
		
	def addFront(self, data) :
		node = Node(data)
		node.next = self.frt
		if (self.frt == None) :
			self.frt = node
			self.Rear = node
		else :
			self.frt.prev = node
			self.frt = node
		self.decSize += 1

	def removeFront(self) :
		if (self.isEmpty() == True) :
			return
		x = self.frt
		self.frt = x.next
		if (self.frt == None) :
			self.Rear = None
		else :
			self.frt.prev = None
		self.decSize -= 1
		x = None
	
	def addRear(self, data) :
		node = Node(data)
		if (self.frt == None) :
			self.frt = node
			self.Rear = node
		else :
			self.Rear.next = node
			node.prev = self.Rear
			self.Rear = node
		self.decSize += 1
		 
	def removeRear(self) :
		if (self.isEmpty() == True) :
			return
		x = self.Rear
		self.Rear = x.prev
		if (self.Rear == None) :
			self.frt = None
		else :
			self.Rear.next = None
		self.decSize -= 1
		x = None
	
	def getfront(self) :
		if (self.isEmpty() == True) :
			print("\n Empty Deque ")
		return self.frt.data
	
	def getrear(self) :
		if (self.isEmpty() == True) :
			print("\n Empty Deque ")
		return self.Rear.data

	def Size(self) :
		return self.decSize
	
if __name__== '__main__':
    d = Deque2()
    d.addFront('cat')
    d.addRear('dog')
    d.addRear(6)
    d.addFront(2)
    d.removeFront()
    d.removeRear()
    print("\nfront element is ",d.getfront())
    print("\nrear element is ",d.getrear())