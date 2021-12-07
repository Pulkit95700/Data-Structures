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
	def remove(self,index_no):
		if index_no == 0:
			self.head = self.head.next
			return
		cur_node = self.head
		for i in range(index_no-1):
			cur_node = cur_node.next
		cur_node.next = cur_node.next.next
	def print_linked_list(self):
		temp = self.head
		arr = []
		arr.append(self.head.value)
		while temp.next:
			temp = temp.next
			arr.append(temp.value)
		print(arr)
	def Skip_I_Delete(self,i,j):
		head = self.head
		new_linked_list = LinkedList()
		if j==0:
			return 
		if i==0:
			return None
		s = i
		n = j
		while head.next:
			if s>0:
				new_linked_list.append(head.value)
				head = head.next
				s=s-1
			else:
				head = head.next
				n=n-1
				if n == 0:
					s = i
					n = j
		if s>0:
			new_linked_list.append(head.value)
		self.head = new_linked_list.head
Linked_List = LinkedList()
for i in range(1,6):
	Linked_List.append(i)
Linked_List.Skip_I_Delete(2,4)
Linked_List.print_linked_list()