from sys import *

class con : 
	def __init__(self):
		print "Cons with single args"
	
	
	# def __init__(self):
		# print "This is the constructor"
		# print "Hello america"
	
	def fun(self ,passed):
		print "This is function  "
		print "The argv is the " +  str(passed)

	
if (__name__ == '__main__'):
	
	c1 = con()
	# c1.fun("caller")
	passed = argv[1]
	read = stdin.readline()
	stdout.write("The read is %s \n" %( read) )
	c1.fun(passed)
	
	
