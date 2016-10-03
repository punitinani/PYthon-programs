class ops :
	
	def __init__(self, name,value=0):
		self.name = name 
		self.number = value
		
	def __add__ (self , y):
		number = self.number  + y
		return ops( self.name,number)
		
	def __str__(self):
		return str(str.number)+ ","+ str(self.name)
	


num1 = ops("Punit " , 2810)	
num2 = num1+ 50
print num2
		