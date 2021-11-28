class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class Linked_list:
	def __init__(self, init_list = None):
		self.head = None
		if init_list:
			for value in init_list:
				self.append(value)
	def search(self,values):
		cur_node = self.head
		while cur_node.next:
			if cur_node.value == values:
				return cur_node
			cur_node = cur_node.next
		return 
	def append(self, value):
		if self.head == None:
			self.head = Node(value)
			return
		else:
			tail = self.head
			while tail.next is not None:
				tail = tail.next
			tail.next = Node(value)
	def print_list(self):
		array = []
		pr = self.head
		while pr:
			array.append(pr.value)
			pr = pr.next
		print(array)
	def remove(self, value):
		if self.head.value == value:
			self.head = self.head.next
			return
		else:
			prev_node = self.head
			cur_node=prev_node.next
			while cur_node.value!=value:
					prev_node=prev_node.next
					cur_node=prev_node.next
			prev_node.next=cur_node.next
		return
	def insert(self, value, pos):
		if pos == 1:
			node = self.head
			self.head = Node(value)
			self.head.next = node 
			return
		else:
			current_node = self.head
			for i in range(pos - 2):
				current_node = current_node.next
			temp = current_node.next
			current_node.next = Node(value)
			current_node.next.next = temp
		return self.head
	def insert_at_head(self,value):
		temp = self.head
		self.head = Node(value)
		self.head.next = temp  
	def reverse(self):
		last_node = self.head
		reverse_linked_list = Linked_list()
		while last_node:
			temp = last_node.value
			reverse_linked_list.insert_at_head(temp)
			last_node = last_node.next
		# print(reverse_linked_list)
		return reverse_linked_list
	def flatten():
		flatten_list = Linked_list()
		node = self.head 
		while self.head
def iscircular(linked_list):
	slow_runner = fast_runner = linked_list.head 
	while fast_runner and fast_runner.next:
		slow_runner = slow_runner.next
		fast_runner = fast_runner.next.next
		if slow_runner == fast_runner:
			return True

# list_with_loop = Linked_list([2, -1, 3, 0, 5])

# # Creating a loop where the last node points back to the second node
# loop_start = list_with_loop.head.next

# node = list_with_loop.head
# while node.next: 
#     node = node.next   
# node.next = loop_start

# small_loop = Linked_list([0])
# small_loop.head.next = small_loop.head
# print ("Pass" if iscircular(list_with_loop) else "Fail")
# print ("Pass" if not iscircular(Linked_list([-4, 7, 2, 5, -1])) else "Fail")
# print ("Pass" if not iscircular(Linked_list([1])) else "Fail")
# print ("Pass" if iscircular(small_loop) else "Fail")
# print ("Pass" if not iscircular(Linked_list([])) else "Fail")
# a = Linked_list()
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# reversed=a.reverse()
# hello=Linked_list()