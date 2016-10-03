class base :
	__h ="Hello world"
	def __base (self):
		print "Inside the Base method that is private" , base.__h
		# self.base()
		
	def base (self):
		self.__base()
		print "Hello world"
		
if (__name__ =="__main__"):
	b= base ()
	b.base ()
	