import functools
def square (number):
	return number * number;
	
	
nums = list(range (1,11))

print nums

sum = lambda x : x * x
# print sum (10);

another = list ( functools.reduce(sum ,range(1 , 500)))
print another;

