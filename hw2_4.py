class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		self.front = self.back = None
		self.qsize = 0

	def isempty(self):
		return self.front == None

	def dequeue(self):
		if self.isempty():
			return
		x = self.front
		self.front = x.next
		if(self.front == None):
			self.back = None
	
	def enqueue(self, item):
		x = Node(item)
		if self.back == None:
			self.front = self.back = x
			return
		self.back.next = x
		self.back = x

	def Size(self):
		return self.qsize

if __name__== '__main__':
	q = Queue()
	q.enqueue(10)
	q.enqueue(20)
	q.dequeue()
	q.dequeue()
	q.enqueue(30)
	q.enqueue(40)
	q.enqueue(50)
	q.dequeue()
	print("Queue's front " + str(q.front.data))
	print("Queue's rear " + str(q.back.data))
	

