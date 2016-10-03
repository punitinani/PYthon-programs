class a (object):
	def __init__(self, name=  None):
		print "This is class a" ,name
		
	def method_a(self) : 
		print "This is  method_a form class blablablablabalblabl"



	def __del__(self) :
		print "Ending a"
		

		
class b(a) :
	def __init__(self , name) :
		#a.__init__( self)
		print  "This is class b" 
		# self.__del__() 
		
		
		
	def method_a (self) :

		print "This is method b"
		super(b,self).method_a()		
		
	# def __del__(self) :
		# print "Ending b"
		
		
if (__name__ == '__main__'):
	a = a()
	b = b("Punit")
	b.method_a()
	# print "HEllo"
	