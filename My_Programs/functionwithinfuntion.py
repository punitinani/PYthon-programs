def punit ():
    print "Hello punit"
    def count ():
            print "Inside the count method"
            return ("Hello")

    return count
	
	
def punit(hello):
	print "This is function overloading" , hello
	return False



def re ():
    a = 10
    b = 22
    c= 33
    d="A string "
    return (a,b,c,d)






def main ():
    """ Always put a main () method processing this will work as the debugging for you"""
    getTheVariable = punit()
    print getTheVariable
    
    a=100
    (A ,B ,C ,D) = re()
    print "A is " , A
    print "B is " , B
    print "C is " , C
    print "D is " , D

    punit("Good or Bad")	
		
	
	


if (__name__ == '__main__'):
    main()
    
else :
    print "Having the check at the work book of the programs"
    


