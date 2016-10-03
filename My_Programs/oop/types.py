from types import MethodType

def play (self):
	print "Playing "  , self.name

def play1 (self):
	print "Playing "  , self.name


class A_class:
	def method_a (self):
		print "Internal call of the funciton func as the method_a"
	def __init__ (self , get):
		print "This is  ", get
		self.name = get
		

if (__name__ == '__main__'):
	# A_class.doingWhat  = MethodType(play , p)  this is for that particular object p
	
	# for whole class
	A_class.doingWhat =play
	p= A_class("Name1")
	p.doingWhat()
	A_class.doingWhat  = MethodType(play1 , p)
	p1 = A_class('Name2')
	p1.doingWhat()
