from collections import deque

class Node(object):

	def __init__(self,value = None):
		self.value = value
		self.left = None
		self.right = None
	
	def get_value(self):
		return self.value
	
	def set_value(self, value):
		self.value = value 
	
	def set_left_child(self, left):
		self.left = left 
	
	def set_right_child(self, right):
		self.right = right 
	
	def get_left_child(self):
		return self.left 
	
	def get_right_child(self):
		return self.right 
	
	def has_left_child(self):
		return self.left != None
	
	def has_right_child(self):
		return self.right != None
	
	def __repr__(self):
		return (f"Node({self.get_value()})")

	def __str__(self):
		return (f"Node({self.get_value()})")

class Tree(object):
		
	def __init__(self, root = None):
		self.root = Node(root)
	
	def get_root(self):
		return self.root 
	
	def set_root(self, node):
		self.root = node

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))	


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
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

que = Queue()
node = tree.get_root()
que.enq(node)
print(que)	

def BFS(tree: Tree):
	visited_node = list()
	q = Queue()
	node = tree.get_root()
	q.enq(node)
	node = q.deq()
	while(node):
		visited_node.append(node)
		if node.has_left_child():
			q.enq(node.get_left_child())
		if node.has_right_child():
			q.enq(node.get_right_child())
		node = q.deq()
	return visited_node

print(BFS(tree))