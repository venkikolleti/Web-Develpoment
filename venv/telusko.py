i=5
while(i>=1):
    print(i)
    i=i-1

i=1
while(i<=3):
    print("venki",end="")
    j = 1
    while(j<=3):
        print("kolleti",end="")
        j=j+1
    i=i+1
    print()

i=1
j = 1
while(i<=3):
    print("venki",end="")
    while(j<=3):
        print("kolleti",end="")
        j=j+1
    i=i+1
    print()

i=1
j = 1
while(i<=3):
    print("venki",end="")
    while(j<=3):
        print("kolleti",end="")
        j=j+1
    i=i+1

for i in range(20,11,-1):
    print(i)

breads=7
x=int(input("enter a number:"))
i=1
while i<=x:
    if i>breads:
        print("out of stock")
        break
    print("bread")
    i=i+1
print("bye")

i=1
while i<=5:
    print(i)
    if i==3:
        break
    i=i+1
print("kolleti")


# i=1
# while i<=6:
#      pass


#arithematic operations
a=eval(input("enter any expression:"))
print(a)
print("byee")

i=101
while(i<=210):
    if(i%5==0):
        continue
    print(i)
    i=i+1



for i in range(1,101):
    if (i%3==0):
        continue
    print(i)

print("venkaiah kolleti")



n=int(input("enter a number for prime:"))
i=2
while i<n:
    if n%i==0:
        print("not a prime")
        break
    i=i+1
else:
    print("it is prime")

n=int(input("enter a num for primeee"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")