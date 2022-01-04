class Node(object):
	def __init__(self,value = None):
		self.value = value
		self.left = None 
		self.right = None
	def set_value(self,value):
		self.value = value 
	def get_value(self):
		return self.value
	def set_right_child(self,right):
		self.right = right
	def set_left_child(self,left):
		self.left = left
	def get_left_child(self):
		return self.left
	def get_right_child(self):
		return self.right 
	def has_right_child(self):
		return self.right != None
	def has_left_child(self):
		return self.left != None
	def __repr__(self):
		return f"""Node({self.get_value})"""
	def __str__(self):
		return f"Node({self.get_value()})"

class Tree(object):
	def __init__(self,value = None):
		self.root = Node(value)	
	def get_root(self):
		return self.root

class State(object):
	def __init__(self,node):
		self.node = node
		self.visited_left = False
		self.visited_right = False
	def get_node(self):
		return self.node
	def get_visited_left(self):
		return self.visited_left 
	def get_visited_right(self):
		return self.visited_right
	def set_visited_left(self):
		self.visited_left = True
	def set_visited_right(self):
		self.visited_right = True
	def __repr__(self):
		s = f"""{self.node}\nvisited left: {self.visited_left}\nvisited right : {self.visited_right}"""
		return s 

class Stack(object):
	def __init__(self):
		self.list = list()
	def push(self,value):
		self.list.append(value)
	def pop(self):
		return self.list.pop()
	def top(self):
		if len(self.list) > 0:
			return self.list[-1]
		else:
			return None
	def is_empty(self):
		return len(self.list) == 0
	def __repr__(self):
		if len(self.list	) > 0:
			s = f"""<top of stack>\n_______________\n"""
			s += "\n_______________\n".join([str(item) for item in self.list[::-1]])
			s += "\n_______________\n<bottom of stack>"
			return s
		else:
			return "<stack is empty>"

# def pre_order_with_stack(tree,debug_mode = False):
# 	visit_order = list()
# 	stack = Stack()
# 	node = tree.get_root()
# 	visit_order.append(node.get_value())
# 	state = State(node)
# 	stack.push(state)
# 	count = 0
# 	while(node):
# 		if debug_mode:
# 			print(f"""loop count : {count}\ncurrent_node : {node}\nstack : \n {stack}""")
# 		count += 1
# 		if node.has_left_child() and not state.get_visited_left():
# 			state.set_visited_left()
# 			node = node.get_left_child()
# 			state = State(node)
# 			stack.push(state)
# 			visit_order.append(node.get_value())
# 		elif node.has_right_child() and not state.get_visited_right():
# 			state.set_visited_right()
# 			node = node.get_right_child()
# 			state = State(node)
# 			stack.push(state)
# 			visit_order.append(node.get_value())
# 		else:
# 			stack.pop()
# 			if not stack.is_empty():
# 				state = stack.top()
# 				node = state.get_node()
# 			else:
# 				node = None	
# 		if debug_mode:
# 			print(f"""loop count: {count}\ncurrent node: {node}\nstack : \n{stack}\n""")
# 	return visit_order

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# pre_order_with_stack(tree,debug_mode = True)

def pre_order_dfs(node: Node):
	if (not node.has_left_child()) and (not node.has_right_child()):
		return [node.get_value()]

	lvl_visited = [node.get_value()]

	if node.has_left_child():
		lvl_visited.extend(pre_order_dfs(node.get_left_child()))
	if node.has_right_child():
		lvl_visited.extend(pre_order_dfs(node.get_right_child()))

	return lvl_visited
print(pre_order_dfs(tree.get_root()))