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

	def __repr__(self):
		q = Queue()
		node = self.root
		if node is None:
			return "<empty>" 
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

def convert_arr_to_binary_tree(arr):
	q = Queue()
	index = 0
	if len(arr) <=0 or arr[index] is None:
		return None
	root = Node(arr[index])
	tree = Tree()
	tree.root = root
	q.enq(root)
	index = 1
	while len(q)>0:
		root = q.deq()
		if not root.has_left_child() and index < len(arr):
			if not arr[index] == None:
				root.set_left_child(Node(arr[index]))
				q.enq(root.get_left_child())
				index += 1
			else:
				index += 1
		if not root.has_right_child() and index < len(arr):
			if not arr[index] == None:
				root.set_right_child(Node(arr[index]))
				q.enq(root.get_right_child())
				index += 1
			else:
				index += 1
	return tree.root 
tree = convert_arr_to_binary_tree([1,2,3,4,5,6,7])
def path_from_root_to_node_rec(root,data):
	if root is None:
		return []
	if root.get_value() == data:
		return [root.get_value()]
	else:
		left_list = [root.get_value()]
		right_list = [root.get_value()]
		
		if root.has_left_child():
			left_list.extend(path_from_root_to_node_rec(root.get_left_child(),data))
		
		if root.has_right_child():
			right_list.extend(path_from_root_to_node_rec(root.get_right_child(),data))
		
		if len(left_list) > 1:
			return left_list
		elif len(right_list) > 1:
			return right_list
		else:
			return []

def test_function(test_case):
    arr = test_case[0]
    data = test_case[1]
    solution = test_case[2]
    root = convert_arr_to_binary_tree(arr)
    output = path_from_root_to_node_rec(root, data)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
data = 5
solution = [1, 2, 5]

test_case = [arr, data, solution]
test_function(test_case)
# Pass
arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
data = 5
solution = [1, 3, 5]

test_case = [arr, data, solution]
test_function(test_case)
# Pass
arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 11
solution = [1, 3, 4, 6, 10, 11]

test_case = [arr, data, solution]
test_function(test_case)
# Pass
arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 8
solution = [1, 3, 5,8]

test_case = [arr, data, solution]
test_function(test_case)