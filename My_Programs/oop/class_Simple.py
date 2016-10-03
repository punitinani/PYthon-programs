class Bank :
	def name(self):
		print ("This is name method")
		
	def __init__(self):
		print "This is constructor"
		
	def name1(self,name):
		print "The name is  %s " %(name)
		
if (__name__ =="__main__"):

	b1 = Bank()
	b1.name()	
	print "\n"
	b1.name1(str(raw_input("Please enter your name:- ")))
