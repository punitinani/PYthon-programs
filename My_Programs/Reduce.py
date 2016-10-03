import functools 

def sum(x): 
	return x +x

numbers = list(range(1,11))
print numbers
sum = functools.reduce( sum(numbers),numbers)
print asd