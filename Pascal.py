from math import *
def nCr(n,r):
	if r>n:
		return None
	else:
		return (factorial(n))/(factorial(n-r) * factorial(r))
def Pascal(n):
	output_list = []
	for i in range(n+1):
		output_list.append(int(nCr(n,i)))
	return output_list

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = Pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")
n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)
n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)
n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)
n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)