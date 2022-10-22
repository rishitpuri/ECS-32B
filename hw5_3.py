class node():
	def __init__(self, element):
		self.element = element
		self.l = None
		self.r = None
		self.ht = 1 

class AVLTree():

	def Height(self, rt):
		if not rt:
			return 0
		return rt.ht 
	def put(self, rt, k):
		if not rt:
			return node(k)
		elif k < rt.element:
			rt.l = self.put(rt.l, k)
		else:
			rt.r = self.put(rt.r, k)
		rt.ht = 1 + max(self.Height(rt.l), self.Height(rt.r))
		return rt       
	def rotateleft(self, z):
		x = z.r
		M = x.l
		x.l = z
		z.r = M
		z.ht = 1 + max(self.Height(z.l), self.Height(z.r))
		x.ht = 1 + max(self.Height(x.l), self.Height(x.r))
		return x
	def rotateright(self, z):
		x = z.l
		N = x.r
		x.r = z
		z.l = N
		z.ht = 1 + max(self.Height(z.l), self.Height(z.r))
		x.ht = 1 + max(self.Height(x.l), self.Height(x.r))
		return x
	def rebalance(self, rt):
		if not rt:
			return 0
		return self.Height(rt.l) - self.Height(rt.r)