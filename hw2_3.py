class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Stack:
	def __init__(self):
		self.h = None
		self.stacksize = 0 

	def IsEmpty(self):
		if self.h == None:
			return True
		else:
			return False
	
	def Push(self,data):
		if self.h == None:
			self.h=Node(data)	
		else:
			nodenew = Node(data)
			nodenew.next = self.h
			self.h = nodenew

	def peek(self):
		if self.IsEmpty():
			return None	
		else:
			return self.h.data

	def Pop(self):
		if self.IsEmpty():
			return None	
		else:
			popnode = self.h
			self.h = self.h.next
			popnode.next = None
			return popnode.data

	def Size(self):
		return self.stacksize
		
s = Stack()

s.Push(1)
s.Push(2)
s.Push(3)
s.Push(4)
s.Push(5)
print("\nTop element is ",s.peek())
s.Pop()
s.Pop()
s.Pop()
print("\nfirst element is ", s.peek())
