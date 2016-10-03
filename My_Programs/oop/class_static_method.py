class apart :
	acc_created=0	
	def __init__(self):
		self.name ="Punit"
		self.age = 19
		apart.acc_created +=1
		print "Account created" , apart.acc_created
		
	@staticmethod 
	def createdAcc():
		# print "Account created " + str(apart.acc_created)
		print "This is a static method" + \
			" Currently 	inside of it"

			
			
if (__name__=='__main__'):
	a = apart()
	b = apart()
	c = apart()
	c.name = 'Inani'
	print vars (c)
	print vars (a)
	print vars (b)
	for names in (a ,b,c):
		print names.name
	
	
	apart.createdAcc()
else :
	print "Nothing executable"
	
	