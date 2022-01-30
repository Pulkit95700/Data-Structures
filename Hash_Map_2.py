import functools

# @functools.lru_cache(maxsize = None)
def staircase(n):
	if n==1:
		return 1
	if n==2:
		return 2
	if n==3:
		return 4
	else:
		return staircase(n-1) + staircase(n-2) + staircase(n-3)
order_again = True
cache = {}
while order_again == True:
	n = int(input("Enter the value of n: "))
	if n in cache:
		print(cache[n])
	else:
		result = staircase(n)
		cache[n] = result
		print(result)
	s = input("Do you want to try it again (Y/N): ")
	s = s.upper()
	if s == "N":
		order_again = False