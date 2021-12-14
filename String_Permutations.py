def str_permute(my_string):
	if len(my_string) == 1:
		return [my_string]
	elif len(my_string) == 2:
		return [my_string, my_string[::-1]]
	else:
		output = []
		f_word = my_string[0]
		sub_str_list = str_permute(my_string[1:])
		temp_string = ""
		for string in sub_str_list:
			for i in range(len(string) + 1):
				temp_string = string[:i] + f_word + string[i:]
				output.append(temp_string)
				temp_string = ""
		return output
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = str_permute(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)
string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)