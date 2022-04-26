from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache_memory = OrderedDict()
        # self.recent_memory = []
        self.num_entries = 0
    def set(self,key,value):
        if self.capacity == 0:
            return "can't perform any task as capacity is zero"
        if key in self.cache_memory:
            value = self.cache_memory.popitem(key)
            self.cache_memory[key] = value
        if self.num_entries < self.capacity:
            self.cache_memory[key] = value
            self.num_entries += 1
        else:
            self.cache_memory.popitem(last = False)
    def get(self,key):
        if key in self.cache_memory:
            # self.recent_memory.append(key)
            return self.cache_memory[key]
        else:
            return -1

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(4))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

