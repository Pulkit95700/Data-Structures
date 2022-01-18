class Node(object):
	
	def __init__(self,value = None):
		self.value = value
		self.left = None
		self.right = None

	def set_value(self,value):
		self.value = value
	
	def get_value(self):
		return self.value
	
	def set_left_child(self,left):
		self.left = left 
	
	def set_right_child(self,right):
		self.right = right 

	def get_left_child(self):
		return self.left 

	def get_right_child(self):
		return self.right 
	
	def has_left_child(self):
		return self.left != None
	
	def has_right_child(self):
		return self.right != None

	def find_node_type(self):
		# 0 for leaf , 1 for having one child , 2 for having two child
		if self.value is None:
			return None
		if not (self.has_left_child()) and not (self.has_right_child()):
			return 0
		elif self.has_right_child() and self.has_left_child():
			return 2
		else:
			return 1

	def __repr__(self):
		return f"Node({self.get_value()})"

	def __str__(self):
		return f"Node({self.get_value()})"

from collections import deque

class Queue():
	def __init__(self):
		self.q = deque()

	def enq(self,value):
		self.q.appendleft(value)

	def deq(self):
		if len(self.q) > 0:
			return self.q.pop()
		else:
			return None
	
	def __len__(self):
		return len(self.q)


	def __repr__(self):
		if len(self.q) > 0:
			s = "<enqueue here>\n________________\n"
			s += "\n________________\n".join([str(item) for item in self.q])
			s += "\n________________\n<dequeue here>"
			return s 
		else:
			return "<queue is empty>"

class Tree(object):
	def __init__(self):
		self.root = None

	def set_root(self,value):
		self.root = Node(value) 

	def get_root(self):
		return self.root

	def compare(self,node,new_node):
		if node.get_value() == new_node.get_value():
			return 0
		elif node.get_value() < new_node.get_value():
			return 1
		else:
			return -1	

	def insert_with_loop(self,new_value):
		node = self.get_root()
		node_inserted = False
		if node is None:
			node.set_value(new_value)
			node_inserted = True
		else:
			while node_inserted is False:
				comparison = self.compare(node, new_node)

				if comparison == 0:
					node.set_value(new_value)
					node_inserted = True
				elif comparison == -1:
					if node.has_left_child():
						node = node.get_left_child()
					else:
						node.set_left_child(Node(new_value))
						node_inserted = True
				else:
					if node.has_right_child():
						node = node.get_right_child()
					else:
						node.set_right_child(Node(new_value))
						node_inserted = True
	def insert_with_recursion(self,value):
		node = self.get_root() 
		if node is None:
			self.set_root(value)
			node = self.get_root()
		else:
			self._insert_with_recursion_rec(node,value)

	def _insert_with_recursion_rec(self,node,value):
		new_node = Node(value)
		comparison = self.compare(node,new_node)
		if comparison == 0:
			node.set_value(value)
		elif comparison == -1:
			if node.has_left_child():
				self._insert_with_recursion_rec(node.get_left_child(),value)
			else:
				node.set_left_child(new_node)
		else:
			if node.has_right_child():
				self._insert_with_recursion_rec(node.get_right_child(),value)
			else:
				node.set_right_child(new_node)
	def Search(self,value):
		node = self.root
		q = Queue()
		q.enq(node)
		output = False
		while len(q) > 0:
			node = q.deq()
			if node.has_left_child():
				q.enq(node.get_left_child())
			if node.has_right_child():
				q.enq(node.get_right_child())
			if node.get_value() == value:
				output = True
				break
		return output
	def min_value_node(self):
		node = self.root 
		while node.has_left_child():
			node = node.get_left_child()
		return node
	def delete(self,value):
		node = self.get_root()
		node = self.Delete_with_rec(node,value)
	def Delete_with_rec(self,node,value):
		if node is None:
			return node
		if value < node.get_value():
			node.set_left_child(self.Delete_with_rec(node.get_left_child(),value))
			return node
		if value > node.get_value():
			node.set_right_child(self.Delete_with_rec(node.get_right_child(),value))
			return node 
		if node.has_left_child() == False and node.has_right_child() == False:
			return None 
		if node.has_left_child() == False:
			temp = node.get_right_child()
			node = None 
			return temp
		elif node.has_right_child() == False:
			temp = node.get_left_child()
			node = None 
			return temp
		leaf_node = self.min_value_node()
		node = self.Delete_with_rec(self.get_root(),leaf_node.get_value())
		node.set_value(leaf_node.get_value())
		return node   
	def __repr__(self):
		q = Queue()
		node = self.root 
		q.enq((self.root,0))
		s = "Tree\n" + str(node)
		level = 0
		visit_order = list()
		
		while len(q) > 0:
			node,level = q.deq()
			max_level = level
			if node.has_left_child():
				q.enq((node.get_left_child(),level + 1))
				visit_order.append((node.get_left_child(),level + 1))
			else:
				visit_order.append(("<empty>",level + 1))
			if node.has_right_child():
				q.enq((node.get_right_child(),level + 1))
				visit_order.append((node.get_right_child(),level + 1))
			else:
				visit_order.append(("<empty>",level + 1))
		pre_level = -1
		for tup in visit_order:
			node,level = tup
			if level == pre_level:
				pre_level = level
				s = s + " | " + str(node)
			else:
				s = s + "\n" + str(node)
				pre_level = level
		return s

tree = Tree()
tree.insert_with_recursion(50)
tree.insert_with_recursion(60)
tree.insert_with_recursion(90)
tree.insert_with_recursion(30)
tree.insert_with_recursion(35)
tree.insert_with_recursion(40)
print(tree)
tree.delete(50)
print(tree)