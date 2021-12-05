class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None
class Stack:
	def __init__(self):
		self.arr = []
		self.num_elements = 0
	def size(self):
		return self.num_elements
	def push(self,value):
		if self.size() == 0:
			self.head = Node(value)
			self.num_elements += 1
			return
		temp = self.head 
		self.head = Node(value)
		self.head.next = temp
		self.num_elements += 1
		return
	def pop(self):
		if self.size() == 0:
			return None
		self.num_elements -= 1
		temp = self.head
		self.head = self.head.next
		return temp.value
	def reverse_stack(self):
		if self.size() == 0:
			return None
		new_stack = Stack()
		for i in range(self.num_elements):
			new_stack.push(self.pop())
		self.head = new_stack.head
	def print_stack(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.value, end=", ")
			cur_node = cur_node.next
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print_stack()
stack.reverse_stack()
stack.print_stack()