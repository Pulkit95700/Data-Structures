class Node(object):
	def __init__(self,value = None):
		self.value = value 
		self.left = None
		self.right = None
	def set_value(self,value):
		self.value = value 
	def get_value(self):
		return self.value
	def get_left_child(self):
		return self.left
	def get_right_child(self):
		return self.right
	def set_left_child(self,left):
		self.left = left
	def set_right_child(self,right):
		self.right = right
	def set_value(self,value):
		self.value = value
	def has_left_child(self):
		return self.left != None
	def has_right_child(self):
		return self.right != None
	def __repr__(self):
		return f"Node({self.value})" 
class Tree(object):
	def __init__(self, value = None):
		self.root = Node(value)
	def set_root(self,value):
		self.root = value
	def get_root(self):
		return self.root
class Stack(object):
	def __init__(self):
		self.list = list()
		self.num_elements = 0
	def push(self,value):
		self.list.append(value)
		self.num_elements += 1
	def pop(self):
		self.num_elements -= 1
		return self.list.pop()
	def is_empty(self):
		return self.num_elements == 0
	def top(self):
		return self.list[self.num_elements - 1]
	def len(self):
		return self.num_elements
	def __repr__(self):
		s = f"<top of stack>"
		s += "\n_____________".join([item for item in self.list[::-1]])
		s += "\n<bottom of stack>"
		return s

def DFS_post_order_traversal(node):
	visit_order = list()

	if node:
		visit_order.extend(DFS_post_order_traversal(node.get_left_child()))
		visit_order.extend(DFS_post_order_traversal(node.get_right_child()))
		visit_order.append(node.get_value())

	return visit_order


tree = Tree()
tree.set_root(Node("apple"))
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


print(DFS_post_order_traversal(tree.get_root()))