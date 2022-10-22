class n:
	def __init__(self, k):
		self.d = k
		self.lft = None
		self.rgt = None

def CheckBST(r, left_node=None, right_node=None):
	if (r == None):
		return True
	if (right_node != None and r.d >= right_node.d):
		return False
	if (left_node != None and r.d <= left_node.d):
		return False
	return CheckBST(r.lft, left_node, r) and CheckBST(r.rgt, r, right_node)

if __name__ == '__main__':
	r = n(4)
	r.lft = n(2)
	r.rgt = n(5)
	r.lft.lft = n(1)
	r.lft.rgt = n(3)
	
	if (CheckBST(r, None, None)):
		print("is BST")
	else:
		print("not a BST")
