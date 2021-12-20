def ch(num):
	return chr(num + 96)
def find_codes(num_data):
	if num_data == 0:
		return [""]
	else:
		remainder = num_data % 100
		output_100 = list()
		if remainder <= 26 and num_data>9:
			output_100 = find_codes(num_data // 100)
			alphabet = ch(remainder)

			for index,element in enumerate(output_100):
				output_100[index] = element + alphabet
		remainder = num_data % 10

		output_10 = find_codes(num_data // 10)
		alphabet = ch(remainder)

		for index,element in enumerate(output_10):
			output_10[index] = element + alphabet 
		output = list()
		output.extend(output_10)
		output.extend(output_100)

		return output


# find_codes(12)
print(find_codes(111111))

