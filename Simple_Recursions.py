def _power(n,power):
	if power>=0:
		if power==0:
			return 1
		else:
			return n*_power(n,power-1)
	elif power<0:
		if n==0:
			return 0
		if power == 0:
			return 1
		else:
			return 1/n * _power(n,power + 1)
def sum_array(array):
	if len(array)==0:
		return 0
	else:
		return array[0]+sum_array(array[1:])
def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)

def Reverse_String(my_string):
    if len(my_string) == 1:
        return my_string
    else:
        rest = slice(1,None)
        return Reverse_String(my_string[rest])+my_string[0]
def is_palindrome(my_string):
    if len(my_string) == 1:
        return True
    elif len(my_string) == 2:
        return my_string[0] == my_string[1]
    else:
        output = (my_string[0] == my_string[len(my_string) - 1]) & (is_palindrome(my_string[1:len(my_string) - 1]))
        return output  

print(sum_array([1,2,3,4,5,6,7,8,9,10]))

print(_power(5,-1))
print(factorial(1))
print(is_palindrome("madam"))
print(Reverse_String("Pulkit"))