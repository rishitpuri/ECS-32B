class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def levelorder(btree):
	
	queue = []
	queue.append(btree)

	while(len(queue) > 0):
		print(queue[0].data)
		node = queue.pop(0)
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)

btree = Node(10)
btree.left = Node(20)
btree.right = Node(30)
btree.left.left = Node(40)
btree.left.right = Node(50)

levelorder(btree)

