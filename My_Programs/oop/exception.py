try :
	a= 10 /0 
except Exception , e:
	print e.message
finally :
	print "Finally is  on command"