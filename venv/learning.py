print("hello world")
a=[1,2,3,4]
a.append(5)
a.insert(1,6)
a.extend([7,8,9])
a[3]=105
print(a)
a=[1,2,3,4,5,6]
#a.remove(5)
#a.pop(3)
#del a[0]
a.clear()
print(a)
a=[2,6,3,56,34,23,12,12,0]
a.sort()
print(a)
a.reverse()
print(a)
a=[1,22,13,4]
a.reverse()
print(a)
a=[12,4,5,66,2]
a.sort(reverse=True)
print(a)
a=["Venki","Ashok","naresh"]
a.sort(reverse=True)
print(a)
a=[1,2,4,5,6]

print(max(a))
print(min(a))




a=(1,3,6,7,19)
print(a[4])

print(a.index(7))
a=(1,3,4,5,4,3,4,2,4)
print(a.count(3))

def add(x,y):
    return x+y

n=int(input("enter a number for prime:"))
i=2
while (i<n):
    if (n%i==0):
        print("not a prime")
        break
    i=i+1
else:
    print("it is prime")

i=101
while(i<=201):
    i = i + 1
    if(i%5==0):
        continue
    print(i)



for i in range(4):
    print("#",end="")
print()
for i in range(4):
    print("#",end="")
print()
for i in range(4):
    print("#",end="")
print()
for i in range(4):
    print("#",end="")
print()
print("venki")



for i in range(4):
    for j in range(4):
        print("#",end='')
    print()
print("end this")


for i in range(4):
    for j in range(i+1):
        print("#", end='')
    print()
print("end this")



for i in range(4):
    for j in range(4-i):
        print("#", end='')
    print()
print("end this")


