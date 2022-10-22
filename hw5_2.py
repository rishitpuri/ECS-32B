import sys
class Maxheap:
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.s = 0
		self.H = [0] * (self.maxsize + 1)
		self.H[0] = sys.maxsize
		self.first = 1
	def p(self, position):
		return position // 2
	def intchg(self, position1, position2):
		self.H[position1], self.H[position2] = (self.H[position2], self.H[position1])
	def insert(self, key):
		if self.s >= self.maxsize:
			return
		self.s += 1
		self.H[self.s] = key
		pre = self.s
		while (self.H[pre] > self.H[self.p(pre)]):
			self.intchg(pre, self.p(pre))
			pre = self.p(pre)
	def getMax(self):
		get = self.H[self.first]
		self.H[self.first] = self.H[self.s]
		self.s -= 1
		return get

if __name__ == "__main__":
	heap = Maxheap(10)
	heap.insert(7)
	heap.insert(10)
	heap.insert(8)
	heap.insert(72)
	print("The Max val is " + str(heap.getMax()))
