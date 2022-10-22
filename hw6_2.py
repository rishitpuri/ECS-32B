class graphadt:
	def __init__(self, vr):
		self.vr = vr
		self.adj = [[] for i in range(vr)]

	def add(self, x, y):
		self.adj[x].append(y)
		self.adj[y].append(x)
	
	def GraphOddDegree(self):
		o = 0
		for i in range(self.vr):
			l = len(self.adj[i])
			if l%2!=0:
			    o+=1
		return o

if __name__ == '__main__':
	
	vr = 8
	a = graphadt(vr)
	a.add(0,1)
	a.add(0,7)
	a.add(0,3)
	a.add(1,2)
	a.add(1,5)
	a.add(2,3)
	a.add(2,4)
	print(' odd degree : ',a.GraphOddDegree())