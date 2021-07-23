# x=input("enter a phone number:")
# while len(x) !=10:
#     print("enter phone number  only")
#     x=input("enter a character:")
#
# print(x)


def a(x,y):
    print("hellow world",y)
    print("good morning",x)
a("bye","hello")

def a(x="user"):
    print("hellow world")
    print("good morning",x)
a("venki")


def a(x,y):
    add=x+y
    print("result:",add)
a(4,5)
a("venki","87")


def a(*x):
    sum=0
    for i in x:
        sum=sum+i
    return sum
result=a(2,4)
print(result)





a=[1,2,3,4,5]
sum=0
for i in a:
    sum=sum+i
print(sum)

def a(**x):
    print(x)

a(name="kolleti",age=17)


a=(1,3,6,8)
print(a[0])
print(a.index(6))

def a(name,age,country="India"):
    print("hello:",name)
    print("Age:",age)
    print("i am from:",country)

a("venki",17)
a("venkaiah",18,"America")

def a(x):
    for k,v in x.items():
        if k=="name":
            print(k,"   :",v)
        elif k=="age":
            print(k,"    :",v)
        elif k=="country":
            print(k,":",v)
        else:
            print(k," :",v)
b={"name":"venkaiah","age":17,"country":"india"}
b["mobile"]="00000000"
a(b)


def a(data):
    print("")
    for k,v in data.items():
        print(k,":",v)
userdata={}
e=1
while e!="0":
    userkey=input("user key:")
    uservalue=input("user value:")
    userdata[userkey]=uservalue
    e=input("enter 0 to end or any key to adding more...")
a(userdata)


def a(x,c):
    return x+c
b=a(5,9)
print(b)
print(a(5,7))


def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
a=[34,67,12,78,232,69]
result=bubblesort(a)
print("sorted list is:",result)

a=eval(input("enter a num:"))
print(a)


