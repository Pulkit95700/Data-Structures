def Max_Sum(my_list):
	maxsum = 0
	for i in range(len(my_list)):
		for j in range(i,len(my_list)):
			test_arr = my_list[i:j+1]
			sub_sum = sum(test_arr)
			maxsum = max(maxsum,sub_sum)
	return maxsum 
# lst = [1,2,-5,-4,1,6]
# print(Max_Sum(lst))
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = Max_Sum(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)