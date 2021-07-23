from array import *
a=array("i",[5,4,-7,2,7])
print(a)

from array import *
a=array("i",[5,4,-7,2,7])
print(a.typecode)

from array import *
a=array("i",[5,4,-7,2,7])
a.reverse()
print(a)

from array import *
a=array("i",[5,4,-7,2,7])
print(a[3])

from array import *
a=array("i",[5,4,-7,2,7])
for i in range(len(a)):
    print(a[i])


from array import *
a=array("i",[5,4,-7,2,7])
for e in a:
    print(e)


from array import *
a=array("i",[5,4,-7,2,7])
b=array(a.typecode,(a for a in a))
for e in b:
    print(e)



from array import *
a=array("i",[5,4,-7,2,7])
b=array(a.typecode,(a*a for a in a))
for e in b:
    print(e)



from array import *
a=array("i",[5,4,-7,2,7])
b=array(a.typecode,(a for a in a))
i=0
while i<len(b):
    print(b[i])
    i=i+1

#user input array

from array import *
a=array("i",[])
b=int(input("enetr the length of array:"))
for e in range(b):
    x=int(input("enter the next value:"))
    a.append(x)
print(a)
print(a.index(x))



