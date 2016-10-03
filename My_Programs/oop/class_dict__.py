class Avengers:
	def count(self) :
		self.name = raw_input("Enter the name ")
		self.fav_grade =(raw_input("Enter the ratting"))
		
	def  __dict__(self):
	
	 return	 "This is " + self.name + " having rates " + self.fav_grade
	 
	def __str__(self):
		print "Inside the str funtion "
		return self.name
	def __del__(self):
		# print "You have deleted the " ,self.__dict__[self.name]
		print "inside the del method"
		
		

if (__name__== '__main__'):
	
	a= Avengers ()
	a.count()
	# print dict(a)
	
	print str(a)
	# del a