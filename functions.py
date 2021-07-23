

#fibonnacci sequence
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(10)



#factorial for a given number.............................................
def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=5
result=fac(x)
print(result)


n=5
f=1
for i in range(1,n+1):
    f=f*i
print(f)



#recuurssion
import sys
print(sys.getrecursionlimit())

#factorial by using recursion.......................................

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(5)
print(result)

a=fact(4)
print(a)
print(fact(5))



#lambda....................................................

x=lambda a,b:a+b
y=lambda a,b:a*b
print(x(5,6))
print(y(5,6))


# filter  map reduce............................................
def is_even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8,96,58,33]
evens=list(filter(is_even,nums))   #filter......................
print(evens)

nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))    #filter...................
print(evens)


nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))        #map.......................
print(evens)
print(doubles)

from functools import reduce
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
sum=reduce(lambda a,b:a+b,doubles)         #reduce..........................................
print(evens)
print(doubles)
print(sum)


#decorates..............................................................
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)


#classs  and   objects..................................................................

class computer():
    def config(self):
        print("hello")

a=computer()
a.config()


class computer():
    def __inti__(self):                 #__init__ method...............
        print("hello rgukt")
a=computer()


class computer:
    charger=1                        #static /class variables
    def __init__(self,ram,rom):
        self.ram=ram                     #instant varibles
        self.rom=rom
    def config(self):
        print("config is",self.ram,self.rom,computer.charger)

com1=computer("8gb","128gb")
com2=computer("6gb","64gb")
computer.charger=5
com1.ram="12gb"

com1.config()
com2.config()



class car():
    def __init__(self):
        self.mil=10
        self.com="bmw"
c1=car()
c2=car()
c1.mil=20
print(c1.com,c1.mil)
print(c2.com,c2.mil)


class car():
    wheels=4
    def __init__(self):
        self.mil=10
        self.com="bmw"
c1=car()
c2=car()
c1.mil=20
car.wheels=8
print(c1.com,c1.mil,car.wheels)
print(c2.com,c2.mil,car.wheels)



#inner classs(class inside a class................................

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.ram,self.cpu)
a=student("venki",54)
b=student("venkaiah",52)
a.show()
b.show()

#Inheritance  ....................................
class A:              #super classs.........
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
            print("feature 2 is working")

class B:    #sub classs..............................
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()

print("print with inheritance easily")
#how we print the above code easily with inheritance.........................
class A:             # parent classss..........................
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
            print("feature 2 is working")

class B(A):                    #child class.............
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()



class A:             #grnad parent class.............................
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
            print("feature 2 is working")

class B(A):         #parent classsss........................
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

class C(B):         #child class                             #we written like C(A,B)  for inhertance both
    def feature5(self):
        print("feature 5 is working")
    def feature6(self):
        print("feature 6 is working")

c1=C()
c1.feature1()
c1.feature3()
c1.feature6()




##constructor......................................................

class A:
    def __init__(self):               #this is constructor.......
        print("from A init")
    def fig1(self):
        print("figure 1 is flower")
class B(A):        # there is no constructor in B class so it will call A constructor.....
        def fig2(self):
            print("figure 2 is fruit")
b1=B()

print("code completed")

#A constructor not showned below by calling B child classss...........
class A:
    def __init__(self):
        print("from A init")
    def fig1(self):
        print("figure 1 is flower")
class B(A):
    def __init__(self):
        print("from B init")
    def fig2(self):
        print("figure 2 is fruit")
b1=B()

print("code completed")
#print child and parent class constructors by this code......................
class A:
    def __init__(self):
        print("from A init")
    def fig1(self):
        print("figure 1 is flower")
class B(A):
    def __init__(self):
        super().__init__()
        print("from B init")
    def fig2(self):
        print("figure 2 is fruit")

b1=B()
print("code completed")

#three classes with constructor........................................

class A:
    def __init__(self):
        print("from A init")
    def fig1(self):
        print("figure 1 is flower")
class B:
    def __init__(self):
        print("from B init")
    def fig2(self):
        print("figure 2 is fruit")

class C(A,B):
    def __init__(self):
        super().__init__()   #by default super method print the 1st super class constructor
        super().fig1()       # by super() command we call  functions alsooo.............
        print("from C init")
c1=C()





###polymorphism..........................................
###Duck typing..............................

class pycharm:
    def execute(self):
        print("duck typing")
        print("santoor")

class laptop:
    def code(self,ide):
        ide.execute()
ide =pycharm()
lap1=laptop()
lap1.code(ide)


class pycharm:
    def execute(self):
        print("duck typing")
        print("santoor")
class editor:
    def execute(self):
        print("nee *  istam")
        print("Expresss")

class laptop:
    def code(self,ide):
        ide.execute()
ide =editor()
lap1=laptop()
lap1.code(ide)


#operater overloading............................................
a=5
b=6
print(type(a))
print(a+b)
print(int.__add__(a,b))

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
s1=student(58,23)
s2=student(22,55)
s3=s1+s2
print(s3.m1)
print(s3.m2)


#method overloading....................................................

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m1=m2
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=student(2,3)
print(s1.sum(5))
print(s1.sum(2,3,4))
print(s1.sum(2,4))



#method overidding......................................................
class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")
a1=B()
a1.show()



#ITERATORS...............................................................

nums=[7,8,9,5]
it=iter(nums)
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print("iterate completed by usinh net its time for forloop")
for i in nums:
    print(i)


class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        val=self.num
        self.num+=1
        return val
values=topten()
print(values)
print(values.__next__())
print("completed")

class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:                # without this else part it will be continue until infinty
            raise StopIteration   #once try with remove this else part
values=topten()
print(next(values))
for i in values:
    print(i)



#GENERATORS.....................................................
def topten():
    yield 5
values=topten()
print(values)
print(values.__next__())


def topten():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
values=topten()
print(values)
for i in values:
    print(i)

#printing the square roots .................
def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n=n+1
values=topten()
for i in values:
    print(i)

print("completed")



#EXCEPTION HANDLING...............................................

a=5
b=2
print(a/b)

a=5
b=0
try:
    print(a/b)
except Exception:
    print("Hey you cannot divide a number by zero")
print("byee")


a=5
b=2
try:
    print(a/b)
except Exception:
    print("Hey you cannot divide a number by zero")
print("byee")

#to know type of error..........
a=5
b=0
try:
    print(a/b)
except Exception as e:
    print("Hey you cannot divide a number by zero",e)  #e will print the wt type of error it was..
print("byee")

# resource close will not in this conditions..........
a=5
b=0
try:
    print("resource open")
    print(a/b)
    print("resource close")
except Exception:
    print("Hey you cannot divide a number by zero")


#resouce close will not print in this type of conditions also................
a=5
b=2
try:
    print("resource open")
    print(a/b)
except Exception:
    print("Hey you cannot divide a number by zero")
    print("resource close")

a=5
b=2
try:
    print("resource open")
    print(a/b)
except Exception:
    print("Hey you cannot divide a number by zero")
finally:
    print("resource close")


# we know some error to find the code error and our asumption error is samee.........

a=5
b=2    # we can use for another output
try:
    print("resource open")
    print(a/b)
    k=int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey you cannot divide a number by zero",e)
except ValueError as e:
    print("Invalid Input:",e)
except Exception as e:
    print("something went wrong............")
finally:
    print("resource closed")


#multi threadinng............................

from threading import *
class hello(Thread):
    def run(self):
        for i in range(2):
            print("hello")
class hi(Thread):
    def run(self):
        for i in range(2):
            print("hi")
t1=hello()
t2=hi()
t1.run()
t2.run()
print("simplee ex for multi threading")


#by sleep
from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(2):
            print("hello")
            sleep(2)
class hi(Thread):
    def run(self):
        for i in range(2):
            print("hi")
            sleep(2)
t1=hello()
t2=hi()
sleep(0.5)
t1.start()
t2.start()



from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(2):
            print("hello")
            sleep(2)
class hi(Thread):
    def run(self):
        for i in range(2):
            print("hi")
            sleep(2)
t1=hello()
t2=hi()
sleep(1)
t1.start()
t2.start()
t1.join()
t2.join()
print("bye")



#file handling.........................................

f=open("mydata","r")
print(f.read())
f=open("mydata","r")
print(f.readline())

f=open("abc","w")
f.write("laptop")
f=open("abc","a")
f.write("hello guys whats going onnn......")
f.write("neekenduku raaaaaaaaaaa")
f.write("have a drink")


f=open("mydata","r")
f1=open("ab","w")
for data in f:
    f1.write(data)


# f=open("images.png","rb")    #once run itt.................
# for i in f:
#     print(i)

f=open("images.png","rb")      # check in location there are two images with different location........
f1=open("myimg","wb")
for i in f:
    f1.write(i)






#LINEAR SEARCH.......................................

pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()["pos"]=i
            return True
        i=i+1
    return False
list=[5,8,4,6,9,2]
n=9
if search(list,n):
    print("Found at",pos)
else:
    print("not found")





# linera search..........................................
pos=-1
def search(list,n):
    i=0
    while(i<len(list)):
        if list[i]==n:
            globals()["pos"]=i
            return True
        i=i+1
    return False
list=[5,8,4,6,9,2]
n=9
if search(list,n):
    print("found at",pos)
else:
    print("not found")


#binary search...............................................................



pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()["pos"]=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
            return False
list=[4,7,8,9,45,67,23,98,345]
n=45
if search(list,n):
    print("found at",pos)
else:
    print("not found")



#bubble sort.............................................................

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                print(nums)
nums=[5,3,4,8,6]
sort(nums)
print(nums)



#selection sort............................................................

def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos=j
                nums[i],nums[minpos]=nums[minpos],nums[i]
                print(nums)
nums=[5,3,4,8,6,9]
sort(nums)
print(nums)































