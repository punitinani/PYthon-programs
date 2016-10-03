def func(self):
	print "This is function func"
	
def play ():
	print "An external function named play"
	
class A_class:
	def method_a (self):
		print "Internal call of the funciton func as the method_a"
		
if (__name__ =="__main__"):
	
	a = A_class()
	a.method_a()
	setattr(A_class , 'method_b' , func)
	
	a.method_b()
	
	b = A_class()
	b.play=play
	
	b.play()
	# if (hasattr(b,"play()")):
		# print "Yes"
	
