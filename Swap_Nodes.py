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
def Swap_Nodes(LinkedList,pos_1,pos_2):
	if pos_1 >= pos_2:
		return None
	cur_pos = 0 
	cur_node = LinkedList.head
	no_loop = 1
	temp = None
	if pos_1 > LinkedList.size() or pos_2 > LinkedList.size():
		return None
	while no_loop < 3:
		if cur_pos == pos_1 and no_loop < 2 :
			l_node = cur_node
		if cur_pos == pos_2 and no_loop < 2:
			r_node = cur_node
		if no_loop == 2:
			if cur_pos == pos_1 - 1:
				temp_1 = l_node.next
				temp_2 = r_node.next
				cur_node.next = r_node
				r_node.next = temp_1 
				
			if cur_pos == pos_2 - 1:
				l_node.next = temp_2
				cur_node.next = l_node
				return
		if cur_node.next == None:
			no_loop += 1
			cur_node = LinkedList.head
			cur_pos = 0
		cur_node = cur_node.next
		cur_pos += 1


arr = [3,4,5,2,6,1,9]
test_list = LinkedList()
for element in arr:
	test_list.append(element)
Swap_Nodes(test_list,4,3)
test_list.print_linked_list()