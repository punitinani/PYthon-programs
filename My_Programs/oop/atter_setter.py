class getter_setter:
	def __init__(self) :
		self.name ="PYTHON"
		self.version =2.7
		self.user ='punit'
		
		
	def check (self):
		return self
		
		
	def update(self):
		pass
		
		
if (__name__ == '__main__'):
	g = getter_setter ()
	print vars (g)
	
	if hasattr (g ,'name' ):
		print "Yes this is true , having the attribute name"
		
	setattr(g, "caller" , "Dummy")
	print vars (g)
	print sorted(g.__dict__)
	
	delattr(g , 'name')
	print vars(g)
	
	
	get = g.check()
	print get
	