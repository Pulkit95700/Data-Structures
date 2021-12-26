def Last_Index(input_list,target):
	if len(input_list) == 1:
		if input_list[0] == target:
			return 0
		else:
			return -1
	else:
		prev_lvl = Last_Index(input_list[1:], target)
		cur_lvl = input_list[0]

		if (prev_lvl == -1) & (cur_lvl != target):
			return -1

		return prev_lvl + 1

print(Last_Index([1,2,2,3],2))
