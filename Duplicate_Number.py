def duplicate_number(lst):
	for number in lst:
		if lst.count(number) > 1:
			return number
	return None
lst = [0,1,2,3]
print(duplicate_number(lst))