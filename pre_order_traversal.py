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
class State(object):
	def __init__(self,Node):
		self.node = Node
		self.visited_left = False
		self.visited_right = False
	def get_node(self):
		return self.node
	def get_visited_left(self):
		return self.visited_left
	def get_visited_right(self):
		return self.visited_right
	def set_visited_right(self):
		self.visited_right = True
	def set_visited_left(self):
		self.visited_left = True
	def __repr__(self):
		s = ""
		s = s + str(Node)
		s = s + f"visited_left : {self.visited_left}"
		s = s + f"visited_right : {self.visited_right}"
		return s
tree = Tree()
tree.set_root(Node("apple"))
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
def DFS_Pre_Order_Traversal(tree : Tree):
	stack = Stack()
	node = tree.get_root()
	state = State(node)
	stack.push(state)
	visit_order = list()
	visit_order.append(node.get_value())
	while node:
		if node.has_left_child() and not state.get_visited_left():
			state.set_visited_left()
			node = node.get_left_child()
			state = State(node)
			stack.push(state)
			visit_order.append(node.get_value())
		elif node.has_right_child() and not state.get_visited_right():
			state.set_visited_right()
			node = node.get_right_child() 
			state = State(node)
			stack.push(state)
			visit_order.append(node.get_value())
		else:
			stack.pop()
			if not stack.is_empty():
				state = stack.top()
				node = state.get_node()
			else:
				node = None
	return visit_order

print(DFS_Pre_Order_Traversal(tree))

