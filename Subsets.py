def Subsets(input_list):
	if len(input_list) == 1:
		return [[],[input_list[0]]]
	else:
		output = []
		subset_list = Subsets(input_list[1:])
		f_element = input_list[0]
		for ele_list in subset_list:
			output.append([f_element] + ele_list)
		output.extend(subset_list)
		return output

print(Subsets([1,2,3,4],end = "")