class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
		self.num_elements = 0
	def append(self,value):
		if self.head == None:
			self.head = Node(value)
			self.num_elements =+ 1
			return
		else:
			cur_node = self.head
			while cur_node.next:
				cur_node = cur_node.next
		cur_node.next = Node(value)
		self.num_elements += 1
		return
	def size(self):
		return self.num_elements
	def pos_node(self,value):
		temp = self.head
		for i in range(value-1):
			temp = temp.next
		return temp.next.value
	def print_linked_list(self):
		temp = self.head
		arr = []
		arr.append(self.head.value)
		while temp.next:
			temp = temp.next
			arr.append(temp.value)
		print(arr)
	def Swap_Nodes(self,pos_1,pos_2):
		cur_node = self.head
		cur_node_pos = 0
		while cur_node.next:
			cur_node = cur_node.next
			cur_node_pos += 1
			if cur_node_pos == pos_1:
				temp = cur_node.value
				cur_node.value = self.pos_node(pos_2)
			if cur_node_pos == pos_2:
				cur_node.value = temp
		return  
arr = [3,4,5,2,6,1,9]
test_list = LinkedList()
for element in arr:
	test_list.append(element)
test_list.Swap_Nodes(3,4)
test_list.print_linked_list()
