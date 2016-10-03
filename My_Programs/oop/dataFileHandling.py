f = open (r"hello.txt" , "r+")

String = str(raw_input ("Enter the content "))
f.write(String)
lines = f.readlines()
f.flush()
f.close()
for i in lines:
	print i