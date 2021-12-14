import copy
def list_permute(lst):
	if len(lst) <= 1:
		return lst 
	elif len(lst) == 2:
		return [lst,lst[::-1]]
	else:
		output = []
		current_level = lst[0]
		prev_list = list_permute(lst[1:])
		for element in prev_list:
			for pos in range(len(element)+1):
				temp_list = []
				temp_element = element.copy()
				for i in range(len(element)+1):
					if i == pos:
						temp_list.append(current_level)
					else:
						temp_list.append(temp_element.pop())
				output.append(temp_list)
		return output 

print(list_permute([1,2,3]))