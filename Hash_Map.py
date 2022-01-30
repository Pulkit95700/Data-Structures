class LinkedListNode(object):
	def __init__(self,key,value):
		self.value = value
		self.next = None
		self.key = key
class HashMap(object):
	def __init__(self):
		self.p = 31
		self.num_entries = 0
		self.bucket_array = [None for _ in range(10)]
	def put(self,key,value):
		new_node = LinkedListNode(key,value)
		bucket_index = self.get_bucket_index(key)
		head = self.bucket_array[bucket_index]
		while head is not None:
			if head.key == key:
				head.value = value
				return 
			head = head.next 
		head = self.bucket_array[bucket_index]
		new_node.next = head
		self.bucket_array[bucket_index] = new_node
		self.num_entries += 1				
	def get(self,key):
		bucket_index = self.get_bucket_index(key)
		head = self.bucket_array[bucket_index]
		while head is not None:
			if head.key == key:
				return head.value
			head = head.next 
		return None
	def get_bucket_index(self,key):
		return self.get_hash_code(key)
	def get_hash_code(self,key):
		key = str(key)
		num_bucket_index = len(self.bucket_array)
		const = 1
		hash_code = 0
		for char in key:
			hash_code = hash_code + ord(char) * const
			const *= self.p 
		return hash_code % num_bucket_index
	def _rehash(self):
		old_num_buckets = len(self.bucket_array)
		old_bucket_array = self.bucket_array
		self.bucket_array = [None for _ in range(old_num_buckets*2)]
		for head in old_bucket_array:
			while head is not None:
				key = head.key 
				value = head.value 
				self.put(key,value)
				head = head.next 
			
	def delete(self,key):
		bucket_index = self.get_bucket_index(key)
		head = self.array[bucket_index]
		previous_node = None
		while head is not None:
			if head.key == key:
				if previous_node is not None:
					previous_node.next = head.next 
				else:
					self.bucket_array[bucket_index] = head.next
				self.num_entries -= 1
				return
			else:
				previous = head
				head = head.next 

