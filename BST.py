from collections import deque

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
	def has_left_child(self):
		return self.left != None
	def has_right_child(self):
		return self.right != None
	def get_left_child(self):
	 	return self.left 
	def get_right_child(self):
	 	return self.right 
	def __repr__(self):
	 	return f"Node({self.get_value()})"

class Queue(object):
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
class BinarySearchTree(object):
	def __init__(self,value = None):
		self.root = value 
	def set_root(self,value):
		self.root = value 
	def get_root(self):
		return self.root 
	def compare(self,value,new_node):
		if new_node == None:
			return 
		if value == new_node.get_value():
			return 0
		elif value < new_node.get_value():
			return -1
		else:
			return 1
	def insert(self,value):
		node_inserted = False
		node = self.root
		if node is None:
			self.root = Node(value)
			return 
		while node_inserted == False:
			comparison = self.compare(value,node)
			if comparison == -1:
				if node.has_left_child():
					node = node.get_left_child()
				else:
					node.set_left_child(Node(value))
					node_inserted = True
			elif comparison == 1:
				if node.has_right_child():
					node = node.get_right_child()
				else:
					node.set_right_child(Node(value))
					node_inserted = True
			else:
				node = Node(value)
				node_inserted = True
	def insert_with_recursion(self,value):
		node = self.get_root()
		if node is None:
			self.root = Node(value)
		else:
			self.insert_with_recursion_rec(node,value)
	def insert_with_recursion_rec(self,node,value):
		comparison = self.compare(value,node)
		if comparison == -1:
			if node.has_left_child():
				self.insert_with_recursion_rec(node.get_left_child(),value)
			else:
				node.set_left_child(Node(value))
		elif comparison == 1:
			if node.has_right_child():
				self.insert_with_recursion_rec(node.get_right_child(),value)
			else:
				node.set_right_child(Node(value))
		else:
			node.set_value(value)
	def Search(self,value):
		node = self.get_root()
		comparison = self.compare(value,node)
		node_found = False
		q = Queue()
		q.enq(node)
		while len(q) > 0:
			node = q.deq()
			if node.has_left_child():
				q.enq(node.get_left_child())
			if node.has_right_child():
				q.enq(node.get_right_child())
			if node.get_value() == value:
				node_found = True
		return node_found

	def min_node_value(self,node):
		if node is None:
			return node
		while node.has_left_child():
			node = node.get_left_child()
		return node
	def Delete(self,value):
		if self.Search(value):
			self.Delete_with_rec(self.get_root(),value)
	def Delete_with_rec(self,node,value):
		if node is None:
			return node
		comparison = self.compare(value,node)
		if comparison == 1:
			if node.has_right_child():
				node.set_right_child(self.Delete_with_rec(node.get_right_child(),value))
		elif comparison == -1:
			if node.has_left_child():
				node.set_left_child(self.Delete_with_rec(node.get_left_child(),value))
		else:
			if node.has_right_child() and node.has_left_child():
				temp = self.min_node_value(node)
				node = self.Delete_with_rec(node,temp.get_value())
				node.set_value(temp.get_value())
			elif not node.has_right_child() and not node.has_left_child():
				node = None
			else:
				if not node.has_left_child():
					node = node.get_right_child()
				else:
					node = node.get_left_child()
		return node

	def __repr__(self):
		q = Queue()
		node = self.get_root()
		level = 0
		q.enq((node,level))
		visit_order = list()
		while len(q) > 0:
			node,level = q.deq()
			if node == None:
				visit_order.append(("<empty>",level))
				continue
			else:
				visit_order.append((node,level))
			if node.has_left_child():
				q.enq((node.get_left_child(),level + 1))
			else:
				q.enq((None,level + 1))
			if node.has_right_child():
				q.enq((node.get_right_child(),level + 1))
			else:
				q.enq((None,level + 1))
		s = "Tree\n"
		pre_level = -1
		for tup in visit_order:
			node,level = tup
			if level != pre_level:
				pre_level = level 
				s = s + "\n" + str(node)
			else:
				s = s + " | " + str(node)
		return s
BST = BinarySearchTree()
BST.insert(10)	
BST.insert(20)
BST.insert(5)
BST.insert(15)
BST.insert_with_recursion(75)
print(BST)
BST.Delete(20)
BST.Delete(10)
print(BST)
print(BST.Search(20.5))