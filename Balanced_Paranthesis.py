class Stack:
	def __init__(self):
		self.stack = []
	def push(self, value):
		self.stack.append(value)
	def size(self):
		return len(self.stack)
	def pop(self):
		if self.size() == 0:
			return None
		else:
			return self.stack.pop()
	def count(self,var):
		return self.stack.count(var)
def balanced_paranthesis(my_string):
	a = Stack()
	for char in my_string:
		if char == "(":
			a.push(char)
		elif char == ")":
			if a.pop() == None:
				return False
	return a.size() == 0
print(balanced_paranthesis("((3^2 + 8)*(5/2))/(2+6)"))