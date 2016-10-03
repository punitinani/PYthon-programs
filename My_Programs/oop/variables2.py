import sys
a= 01	
class another :
	a= "Hack"
	b ="the"
	c ="World"
	def __init__ (self):
		self.a ='SCOT'
		self.b = 19
		self.c = 'GOOD'
		print self.a  + " is " +  str ( self.b) + " years old  "  + "He is not " + str (self.c)  + " in the chess "
	
		print " a is " ,a
		print another.a , another.b ,another.c
	""" This is the main start method """
	
	
if (__name__  ==  '__main__'):
	
	a= another()
	print "This is the end of the program "
	print sys.argv[:]