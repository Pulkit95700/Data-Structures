class Node(object):
	def __init__(self, value):
		self.value =  value
		self.next =   None
	def __repr__(self):
		return str(self.value)
class LinkedList:
	def __init__(self,head):
		self.head = head
	def append(self, value):
		if self.head == None:
			self.head = Node(value)
			return
		cur_node = self.head
		while cur_node.next:
			cur_node = cur_node.next
		cur_node.next = Node(value)
	def flatten_deep(self):
		value_list = []
		node = self.head
		while node.next:
			value_list.append(node.value)
			node = node.next
		value_list.append(node.value)
		return value_list

def merge(linked_list_1, linked_list_2):
	joint_linked_list = LinkedList(None)
	if linked_list_1 == None:
		return linked_list_2
	elif linked_list_2 == None:
		return linked_list_1
	node1 = linked_list_1.head
	node2 = linked_list_2.head
	while node1 is not None or node2 is not None:
		if node1 == None:
			joint_linked_list.append(node2)
			node2 = node2.next
		elif node2 == None:
			joint_linked_list.append(node1)
			node1 = node1.next
		elif node1.value <= node2.value:
			joint_linked_list.append(node1)
			node1 = node1.next
		else:
			joint_linked_list.append(node2)
			node2 = node2.next
	return joint_linked_list
class NestedLinkedList(LinkedList):
	# def flatten(self):
	# 	value = []
	# 	for elements in self.flatten_deep():
	# 		value.append(element.flatten_deep())
	# 	value = [item for sublist in value for item in sublist]
	# 	value.sort()
	# 	return value
	def flatten(self):
		return self._flatten(self.head)
	def _flatten(self, node):
		if node.next == None:
			return merge(node.value, None)
		return merge(node.value, self._flatten(node.next))

# def merge(linked_list_1, linked_list_2):
# 	if linked_list_1 == None:
# 		return linked_list_2
# 	if linked_list_2 == None:
# 		return linked_list_1					This will use more time complexity because it contains many loops
# 	join_linked_list = LinkedList(None)
# 	node1 = linked_list_1.head
# 	node2 = linked_list_2.head 
# 	values = []
# 	while node1.next:
# 		values.append(node1.value)
# 		node1 = node1.next
# 	values.append(node1.value)
# 	while node2.next:
# 		values.append(node2.value)
# 		node2 = node2.next
# 	values.append(node2.value)
# 	values.sort()
# 	for elements in values:
# 		join_linked_list.append(elements)
# 	return join_linked_list

linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
    
# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 3 5
    print(node.value)
    node = node.next
nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next