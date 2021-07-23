"""n=int(input("enter a number"))
c=0
for i in range(1,n+1):
    if(n%i==0):
        print(i)
        c = c + 1
#print("count the prime numbers",c)

n=int(input("enter n vaue"))
i=1
while(i<=n):
    if(n%i==0):
        print(i)
    i=i+1

n=int(input("enter a num"))
for i in range(2,n):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("it is prime")

n=int(input("enter any value"))
i=2
while(i<n):
    if(n%i==0):
        print("not a prime")
        break
    i=i+1
else:
    print("it is prime")"""


class A:
    x="something"

class B(A):
    y="nothing"

obj=B()
print(obj.x)
print(obj.x,obj.y)
print(10==88)
print(10<30)
x=pow(2,6)
print(x)

import datetime
a=datetime.datetime.now()
print(a.time)

import math
x=math.sqrt(2)
print(x)


a=5
print(type(a))
b="venki"
print(type(b))
c=[1,2,3]
print(type(c))
d=(2,4,6,7,9)
print(type(d))
e={1,2,3}
print(type(e))
f={"name":"kolleti"}
print(type(f))

a="rgukt rkv rgukt rkv"
print(a)
#print(a.split())
print(a.split())
print(a.split("10"))