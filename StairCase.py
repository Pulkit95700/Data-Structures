def staircase(n):
	if n==0:
		return 1
	elif n<0:
		return 0
	else:
		climb_ways = 0
		climb_ways += staircase(n-1)
		climb_ways += staircase(n-2)
		climb_ways += staircase(n-3)
		return climb_ways

print(staircase(4))