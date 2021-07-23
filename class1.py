'''n=int(input("enter  a num:"))
i=2

while(i<n):
    if(n%i==0):
        print("not a prime")
        break
    i=i+1
else:
    print("it is prime")

# ,7/2,7/3,7/4 7/5 7/6 7/7
#10/2 10/3 10/4 10/5 10/6 10/7 10/8 10/9


# n=int(input("enter  a num:"))
# i=1
#
# while(i<=n):
#     pass



# range(start,end,step)
# range(start,end)
# range(end)

for i in range(1,10,2):
    print(i)

for i in range(6):
    print(i+2)

names="venkaiah"
for i in names:
    print(i)

n=int(input("enter any number:"))
for i in range(1,n+1):
    print(i)


for i in range(5):
    print(i)
else:
    print("no items left")


for i in range(1,6):
    for j in range(i):
        print("*",'',end='')
    print()


a=int(input("enter anything:"))
b=int(input("enter something:"))
c=a+b
print(c)


a=input("enter anyehere:")
print(len(a))



x=input("enter any character:")
while len(x)!=1:
    print("enter one char only")
    x = input("enter any character:")
print(x)'''



def a(*x):
    sum=0
    for i in x:
        sum=sum+i
    print(sum)
    print(x[2])

a(2,3,4,5,6,7)


def a(name="jhj",age="16",country="india"):
    print("hello",name)
    print("Age",age)
    print("i am from",country)
a("venki",16)
a("venkaiah",17,"america")
a()


def a(*x):
    print(x)

a("venki",18,"rguktian")

def a(**x):
    print(x)
    for k,v in x.items():
        print(k,":",v)

a(name="venki",age=18,collage="rguktian")



def add(x,y):
    return(x+y)
result=add(5,10)
print(result)


add=lambda a,b:a+b
print(add(3,9))


def a():
    x="hello"
    print(x)
    def b():
        print("ohh",x)
    b()
a()

x="hello"
def a():
    print(x)

a()
print(x)






















