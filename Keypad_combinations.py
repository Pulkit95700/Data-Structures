def keypad_combinations(num):
	my_keypad = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
	num_str = str(num)
	if num_str.isnumeric() == False:
		return None
	if "0" in num_str or "1" in num_str:
		return None
	if len(num_str) == 1:
		return [char for char in my_keypad[int(num_str)]]
	f_keypad = num_str[0]
	output = []
	key_string = keypad_combinations(num_str[1:])
	for element in key_string:
		for f_key in my_keypad[int(f_keypad)]:
			output.append(f_key + element)
	return output

print(keypad_combinations(23))