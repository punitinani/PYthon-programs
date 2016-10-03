a = {"Punit" :0 , 1:"B" , 0 : "c"}

for i in a :
	print a[i]	
	print i

m ={x: (x*2) for x in range(4)}
print "Befor : "  ,m
# del m
print "After : " ,
# print m

m.pop(1)

print m



d= {k: v for (k,v) in zip (['a','b','c'],[1,2,3])}

print d


d = dict.fromkeys(['a','b','c'],0)

print d

print d.items()