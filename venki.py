"""a={"name":"venki","age":16,"country":"india"}
print(a)
a["age"]=18
print(a)
a["class"]="s16"
print(a)
a.update({"country":"america"})
print(a)
a.update({"gender":"male"})
print(a)
a.pop("age")
print(a)
a.popitem()
print(a)
del a["name"]
print(a)
#print(a)

a.clear()
print(a)
a={'name': 'venki', 'age': 18, 'country': 'america', 'class': 's16', 'gender': 'male'}
print(a.keys())
print(a.values())
if "age" in a:
    print("yes it is")
else:
    print("no isnt")





ashok=37
if ashok==35:
    print("you passed")
elif ashok>35:
    print("you promoted")
    if ashok>75 and ashok<85:
        print("you got good marks")
    elif ashok>=85 and ashok<95:
        print("you got great marks")
    elif ashok>=95:
        print("you are the best")
    else:
        print("you got an average marks")

else:
    print("you failed")


marks=86
if marks==35:
    print("you passed")
elif marks>35:
    print("you promoted")
elif marks>75:
    print("you got good")
elif marks>85:
    print("you got great")
else:
    ("you lost")


i=1
while (i<=100):
    print(i)
    i=i+1

n=int(input("enter a number"))
i=1
while(i<=n):
    if(i%2==0):
        print(i)
    i=i+1

for x in range(6):
    print(x+4)

n=int(input("enter a number"))
i=1

while(i<=n):
    if(n%i==0):
        i=i+1
#print(i)

n=int(input("Enter n Value:"))
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
    print(c)
print("count of factors is ", c)


for i in range(1,100):
    if (x%i==0):
        print(i)"""

print(__name__)
if (__name__=='__main__') :
    print("run only in venki")

class vivo:
    x=34
    def a(s):
       print(s.x)
obj=vivo()
obj.a()
vivo.a(obj)

class oppo:
    def __init__(self):
        self.s="x"
        self.n="y"
        self.i="z"

    def a(self):
        print("vivo",self.s, "info:")
        print("MODEL-",self.s)
        print("RAM  -", self.n)
        print("ROM  -", self.i)
        print('')
b=oppo()
b.s="v20"
b.n="8gb"
b.i="128gb"
b.a()

c=oppo()
c.s="x50"
c.n="16gb"
c.i="256gb"
c.a()




class Bike:
    tyres=2
    def __init__(self):
        self.name="bikename"
        self.year="2020"
        self.mileage="70kmpl"

bike1=Bike()
print(bike1.name,bike1.year,bike1.mileage,Bike.tyres)
print('')
bike2=Bike()
bike2.name="glamour"
bike2.year="2000"
bike2.mileage="80"

Bike.tyres=5
print(bike2.name,bike2.year,bike2.mileage,Bike.tyres)

