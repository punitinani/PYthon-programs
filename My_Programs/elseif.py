print("Enter any integer value")
a = int(raw_input())
print("You have entered " + str(a));
# Checking  the values of the a
if (a > 10):
	print("a is grater than 10");

elif (a==10):
	print("a is equal to 10")

elif (a < 10): 
	print("A is less than 10")
	print (str(sys.argv[1]));

x='foo';


liss =["Hello" , "India" ,"This" ,"Is" ,"punit"]
print (liss[0])

tuple =("Hello" , "India" ,"This" ,"Is" ,"punit")
print (tuple[2])

tuple = tuple

tuple1= ("Hi" ,"Again ")

tuple1 = tuple + tuple1
print(tuple1)
x=0;

print (type(x))

print(2**2)


a=False

print (a)

if (True):
	print(str(a) + "is true")
	
else :
	print(str(a) + "is false")



def punit ():
	a =10
	print ("This is a function",)
	print ("From the punit deshboard",);
	print ("Hello form the desktop")	
	return a,010

a, b = punit()

print "Helloo",a + b
print "Hello" ,10



a = input ()

print a