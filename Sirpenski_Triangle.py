from functools import lru_cache
@lru_cache
def factorial(n):
	if n<=1:
		return 1
	s = 1
	for i in range(1,n+1):
		s = s*i
	return s 
def nCr(n,r):
	return factorial(n)/factorial(n-r)/factorial(r)
def Sirpenski(n):
	for i in range(n+1):
		for k in range(n-i):
			print(end=" ")
		for j in range(i+1):
			if nCr(i,j) % 2 == 1:
				print("*",end="")
			else: 
				print(end=" ")
			print(" ",end="")
		print()
Sirpenski(15)