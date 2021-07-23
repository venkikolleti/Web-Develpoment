# ..................BASIC ARTHEMATIC OPERATIONS.............................................
a=5
b=10
c=22
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)    #gives the int float value
print(a%b)
print(a+b*c)    # followed this operation by BADMAS rule
print((a+b)*c)    #we will put in between bractes for do operation first its also BADMAS rule



#...................TO KNOW THE MEMORY LOCATION ..................................
a=11
b=22
print(id(a))
print(id(b))
print(id(11))   # same number have same location here a=11,11 location is same

print(int(True))  # by default in python int True value is 1
print(int(False))  #by default in python int False value is 0



#print(helloworld)    #by default we cannot print any string or text without two end cods
print("hello world")


#..................BOOLEAN................................

print(10==9)
print(10<20)
print(bool(1))
print(bool(0))             #except zero all numbers are true

#.....................NUMBERS CONVERSION ONE TO ANOTHER.........................................
print(bin(25))    # decimal to binary

print(0b0101)    #binary to decimal

print(oct(25))   #decimal to octal

print(hex(25))   #decimal to hexal
print(hex(10))

print(0xf)   #hex to decimal

print(~12)    #complement(~)

print(12&13)  #Bitwise AND operator

print(12^13)  # xor

print(10<<2)  #left shifted (first we convert 10 into binary after we left shift two zeroes after we will find decimal to that )



#.............................MATHEMATICAL EQUATIONS.........................................

import math
print(math.sqrt(25))   #for finding square root
print(math.floor(2.9))  #for round off of two before value
print(math.ceil(2.2))   #round off to the next value
print(3**2)
print(math.pow(4,2))   # power of any value (first value is base second value is index or power)
print(math.pi)         #constant pi value
print(math.e)         #constant e value
x=abs(-9)             #to change the sign value negative to positive only it will not work for +ve to -ve
print(x)
#print(help("math"))  # for know about the complete math package


#......................DATA TYPES...............................................................
a=3    #int data type
b=3.2    #float data type
c="venki"   # string datatype


#.........PRINTING VALUES BY INDEX NUM...............................

#index number always reprsented in [] square brackets only

name="rguktrkv"
print(name[1])
print(name[-5])
print(name[0:4])    # print some range of index values
print(name[1:])    #in range of data end value not considered above 4 not considered print till only
print(name[:4])    # so we place next index number for print the before value
print(len(name))   # to know the length value



#................MULTIPLE ASSIGNMENTS........................
a,b,c=1,3.8,"string"
print(a,"and",b,"and",c)


#if the string value is like letter not numbers we cant change the string value to integer value
#but integer value easily chages to string value
x=10
y="rollno:"
print(y+str(x))    #convert one data type to another data type

a="65"
print(int(a))    # here we chage string to int beacuse the value is in numbers form




#......................PYTHON LISTS .......................................................................
#List is represented with in the []square bractes
#allows duplict values means repeated values
#list adding values methods.................

a=[1,2,3,"python",7.9]     # allow different types of data types int,float,strings...........
print(a[3])
a.append(66)       #we append or we add a new value to the list at end  of list
print(a)                   #by the help of append we can add value exactly one only

b=[1,2,3,4]
b.insert(1,"apple")     #by using insert we add one value to the list at any place by index number
print(b)                  #here first argument contains the index num and second argument contrain the insert value


c=[1,2,3,4]
c.extend([5,6,7])    # extend is used to add more values to the list
print(c)             #in extend the values added at the end of list

d=[1,2,3,4,5]
d[3]=10          #to change or replace with another value we use this pattern
print(d)
d[0:2]=11,22    #to change the range of values
print(d)


#different method to remove values from list...................

a=[1,2,3,4]
a.remove(2)      #remove values by giving the number what we remove
print(a)         #the given number is removed


b=[1,2,3,4,5]
b.pop(0)         #remove the value by index number
print(b)

c=[11,22,33,44]
del c[1]   # delete value by index number
#del c     #by this completely list is deleted it will show while run it because there no with that that will be completely deletd
print(c)

d=[1,22,333,4444]
d.clear()         #remove the all items in the list
print(d)           #list is there with empty list not deleted


#arranging list in order.............
a=[1,4,8,67,45,3]
a.sort()           #this is for ascending order
print(a)        #lower to higher

b=[1,222,6,9,3,5]
b.sort(reverse=True)        #for decending order
print(b)

c=[2,4,7,9,34,67]
c.reverse()        #this will reverse the value
print(c)           #ex for right to left values reversed


d=[2,4,6,80,34,124]
print(min(d))            #to know minimum value from list
print(max(d))            #to know th maximum value from list

a=[1,2,3,2,12,3]
a.count(2)                #to count the number of times the number will be repeated
print(a)




#.......................TUPLE TYPE.............................................
#tuple will represented in () curley bractes
#tuple values doesnt change directly
#allows duplict values means repeated values

a=(1,2,3,4)
print(a[1])      #call any number by index value

a=(1,22,33,44)
print(a.index(22))       #to know the index value

a=(1,2,3,4,2,3,1,2,2)
print(a.count(2))       #to count the number of times a value repeated


#change the tuple values........
a=(1,2,3,4)
b=list(a)        #here tuple will changes to list form
b[2]=10          #once it will convert to list we use all list commands to it like append,insert,remove ,etc
a=tuple(b)       #here again list changes to tuple
print(a)


#..........................SET TYPE.......................................{  }
#set is a data type with unchangable, means we cant change the values
# unorder, no order of printing output print randomly
# unindex,beacuse of unorder it has no index values

a={1,2,3,5,"python",5.4}
print(len(a))
print(a)       #output values not exact place in like set input it will changes its order

a={1,2,34,2,1,3,1}
print(a)               #this doesnt allows dupilct values ,means doesnt allow repeated values refers in output




#.........................DICTIONARY TYPE....................................................{   }
#dictionary is a data type with the {keyname:keyvalue}
#no index  , unorder in old versions like 3.6,   order in latest 3.7 version


a={"name":"venky","age":17,"country":"india","mobile":"realme"}
print(a)
print(a["name"])         #call by key name

a["mobile"]="realme6"        #replace or change any value
print(a)
a["collage"]="rgukt"
print(a)                     #to add new key and value

a.update({"name":"venki kolleti"})
print(a)                            #change value another method

a.update({"school":"ZPHS Pallam"})
print(a)                               #too add new one


b={'name': 'venki kolleti', 'age': 17, 'country': 'india', 'mobile': 'realme6', 'collage': 'rgukt', 'school': 'ZPHS Pallam'}

print(b.keys())                    #to print all keys in dictionary
print(b.values())                 #to print all values in dictionary


b.pop("age")
print(b)              #remove a item by key name

b.popitem()           #remove the last item
print(b)

del b["name"]           #delete a item by key name
print(b)

#del b             to delete complete dictionary

b.clear()              #clear all data from dictionary but dictionary is there with empty items
print(b)




#......................USER INPUT........................................................................
#deauflt input value is in string format
#this content in user input will be comment out remove triple codes at below start and end to run this part
'''
a=input("enter anything:")        #to take input from the user
print(a)

a=int(input("enter a num"))            #to take integer type data as input
print(a)

x=input("enter any something")
print(len(x))                          #to know the length of input
print(x[0])                               #to print first letter from the input


#to take only 1 character from the user
x=input("Enter any character:")
while len(x) !=1:                                    #this loop will repeate until the user enter one character
    print("please enter one character only")        
    x=input("Enter one character only:")
print(x)

'''




#.....................CONDITIONAL STATEMENTS..........................................................

#to check pass or fail?
# if -else condition.......
marks=35
if marks>=35:
    print("you passed")
else:
    print("you failed")


# if -elif -else condition.........
marks=34
if marks==35:
    ("you are promoted")
elif marks>35:
    print("you passed the exam")
else:
    print("you failed")

# if-elif-if-else condition.....nested if........
marks=78
if marks==35:
    print("you promoted")
elif marks>35:
    print("you passed")
    if marks>75:
        print("you got good marks")
else:
     print("you failed")


#nested if-elif.................
marks=99
if marks==35:
    print("you promoted")
elif marks>35:
    print("you passed")
    if marks>=75 and marks<=85:
        print("you got good marks")
    elif marks>85 and marks<=95:
        print("you got great marks")
    elif marks>95:
        print("you got best marks")
else:
    print("you failed")


#LOOPING......................MEANS REPEATIIG

#............................WHILE LOOP .................................................
#to print numbers upto n....
i=1
#n=int(input("enter a number))
while i<=3:           # 3 is replace by n to print loop from the user input
    print(i)
    i=i+1      #increment


#to print numbers reverse greater to lower?
i=5
#i=int(input("enter a number)) to know range from user
while i>=1:
    print(i)
    i=i-1           #decrement
else:
    print("byeeee")              #once completed while loop it will go for else part

#nested loop ......
i=1
j=1
while i<=3:
    print("rgukt")

    while j<=3:                   #nested while
        print("hello world")
        j=j+1
    i = i + 1
print("competed this one")



#print even numbers upto n........
n=10
i=1
while i<=n:
    if i%2==0:
        print(i)
    i=i+1



#else in while loop.....................

i=1
while i<=3:
    print(i)
    i=i+1
else:
    print("good bye............................")



# t0 check the loop reaches to our given number...

i=1
while i<=5:
    if(i==3):
        print("i reaches oto 3")
    print(i)
    i=i+1
else:
    print("okay stop here....................")

# to check our loop reaches or doesnt reaches to our given number.....

i=1
while i<=5:
    if(i==3):
        print("i reaches oto 3")
    else:
        print("i doesnt reaches to 3")
    print(i)
    i=i+1
else:
    print("okay stop here....................")



#prime numbers upto n.........

n=11
i=2                #every number is divisible by 1 so here we take starting value as 2
while (i<n):
    if(n%i==0):
        print("not a prime")
    i=i+1
else:
    print("it is prime")


#factors for given number.......
n=10
i=1
s=0
while i<=n:
    if n%i==0:
        print("factor is",i)
        s=s+1
    i=i+1
print("number of factors for a given number",s)

#understanding for columns and rows printig
i=1
while i<=3:                    #this show the number of rows   horizontally number of rows
    print("rgukt"," ",end="")
    i = i + 1
    j=1
    while j<=3:                    #this shows number of coloumns  vertically number of rows
        print("hello world","",end="")
        j=j+1

    print()



#break statement in while loop

i=1
while(i<=4):
    print(i)
    if(i==2):
        break
    i=i+1
else:                  #else part doesnt work wgile using break because it will be break the complete code
    print("successfully break the statement......")




# ..................................FOR LOOP ............................................
# in for loop we use range   ,by default range will start from zero......
# range(start,end,step)    when three arugments were passed
#range(start,end)     when two arguments were passed
#range(end)          when one argument were passed


#print n numbers.?
for i in range(1,10,2):           #from lower to h=higher
    print(i)

for i in range(20,10,-2):       #from higher to lower
    print(i)

x=[1,3,6,8,"rgukt",3.9]
for i in x:
    print(i)

x="rgukt"
for i in x:
    print(i)
else:                      #once completed for loop it go to else part
    print("byeeee")


#prime number or not...............
n=7
for i in range(2,n):
    if n%i==0:
        print("not a prime")
        break
else:
    print("it is prime")


#factors for a given number........

n=10
i=1
s=0
for i in range(i,n+1):
    if n%i==0:
        print(i)
        s=s+1
print("count the factors",s)




# ....................BREAK STATEMENT...........................

breads=3
#x=int(input("enter how many breads you want:"))
x=5
i=1
while i<=x:
    if i>breads:
        print("out of stock")
        break                    #break statement is used to stop the further execution
    print("bread")               #once we use break statement else part also doesnt print
    i=i+1
print("byeeee")



#.................PASS statement.....................
#i=1                       #nothing print by passss
#while i<=5:              #pass statement will pass the statement without error
    #pass             #sometime we dont write itself now but we add content sometimes later than that times we use this pass


#...............CONTINUE STATEMENT..........................

for i in range(1,10):
    if(i%3==0):
        continue     #here continue the loop means skip that value and loop runs assually..
    print(i)

i=0
while i<=5:
    i=i+1
    if i==4:
        continue
    print(i)




# ..........................ARRAY .................................

# array is also just like a list
from array import *
val=array("i",[5,7,2,6])
print(val)

#to know the address and length of array...
from array import *
val=array("i",[5,6,8,9,1])
print(val.buffer_info())           #giving the  array address and length of array
print(val.index(6))               #to know the index value

#to know the type of code.....
from array import *
val=array("i",[5,6,8,9,1])
print(val.typecode)           #giving the type of code


#to reverse the code......
from array import *
val=array("i",[5,6,8,9,1])
val.reverse()
print(val)

#To print the value by index number....
from array import *
val=array("i",[5,6,8,9,1])
print(val[0])             #using index number


#print array valuess by for loop....
from array import *
val=array("i",[5,6,8,9,-3])
for i in range(len(val)):
    print(val[i])

#alphabets in array......
from array import *
val=array("u",["a","t","j","v"])
for i in val:
    print(i)


#one array list values passes  to another array list........

from array import *
val=array("i",[3,5,56,8])
newarr=array(val.typecode,(a for a in val))
for e in newarr:
    print(e)

#to square the array values and passes to new array...........
from array import *
val=array("i",[3,5,56,8])
newarr=array(val.typecode,(a*a for a in val))
for e in newarr:
    print(e)


#while loop for print array values one by one.................

from array import *
val=array("i",[3,5,56,8])
i=0
while i<len(val):
    print(val[i])
    i=i+1



#.....................USERINPUT ARRAY............................................................

# from array import *
# arr=array("i",[])
# n=int(input("enter the length of the array:"))
# for i in range(n):
#     x=int(input("enter the next value"))
#     arr.append(x)
# print(arr)


#to know the index value by user input

# from array import *
# arr=array("i",[])
# n=int(input("enter the length of the array:"))
# for i in range(n):
#     x=int(input("enter the next value"))
#     arr.append(x)
# print(arr)
# val=int(input("enter the value for search:"))      #giving the index number for searching value
# k=0
# for e in arr:
#     if e==val:
#         print(k)
#         break
#     k=k+1



#........................NUMPY  .......................its also like array

from numpy import *
arr=array([1,2,3,4])
print(arr)
print(arr.dtype)              #to know data type

#by add one float value all values changes to float vlaue
from numpy import *
arr=array([1,2,3,4,5.6])
print(arr)

#to print the float type values to integers type
from numpy import *
arr=array([1,2,1.9,4,5.3],int)
print(arr)


#......................LINSPACE..........................
# contain three arguments  linspace(start,end,number of parts)
#we cant give number of parts third argument it will default divide 50 parts any range
#end value also considered in it

from numpy import *
arr=linspace(0,5,6)
print(arr)


#..................ARANGE..............................
#arange is also like range aswell
#arange(start,end,step)

from numpy import *
arr=arange(1,10,2)
print(arr)


#..........LOGSPACE.....................

from numpy import *
arr=logspace(1,10,5)         #divide 1 t0 10 into 5 parts
print(arr)
print("%2f"%arr[1])         #print 1 th index value


#...............ZEROES................................
#pritn zeroes n times
from numpy import *
arr=zeros(5)
print(arr)

##...............ONES..................................
#to print 1 s n times
from numpy import *
arr=ones(5)
print(arr)


#a small process...........
from numpy import *
arr=array([1,2,3,4,5])
arr=arr+5                 #added 5 to exach value in array
print(arr)


#........................ADDITION OF ARRAY VALUES....................................
from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([2,45,7,93,4])
arr=arr1+arr2
print(arr)



from numpy import *
arr=array([1,2,3,4,5])
print("sin values :",sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))
print(sort(arr))


#print two different arrays in one array...............................
from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([4,6,9,2,5])
print(concatenate([arr1,arr2]))     #using concatenate two arrays combine as single array


# passes one array elements to another array and observe their locations
from numpy import *
arr1=array([2,5,8,1])
arr2=arr1               #we pass arr1 values to arr2 also
print(arr1)
print(arr2)
print(id(arr1))        #location of arr1 and arr2 are same because of both have same elements
print(id(arr2))


# passes one array elements to another array and observe their locations

from numpy import *
arr1=array([2,5,8,1])
arr2=arr1.view()          #we pass arr1 values to arr2 also
print(arr1)              #by using .view() we change their location memory but elements are same
print(arr2)
print(id(arr1))        #location of arr1 and arr2 are different
print(id(arr2))


#SHALLOW COPY............................................
#in shallow copy we passes one array items another array and here by changing one element it effect on both arrays
from numpy import *
arr1=array([2,5,8,1])
arr2=arr1.view()            #we pass arr1 values to arr2 also
arr1[1]=7                  #by this both arrayS 1 index number will changes to 7
print(arr1)
print(arr2)



#..................................DEEP COPY..........................................

#by changing one item in array it will not effect on another array list.....................
from numpy import *
arr1=array([2,5,8,1])
arr2=arr1.copy()           #we pass arr1 values to arr2 also
arr1[1]=7                  #by this deep copy only arr1 1 index number changes to 7 it will not effect on arr2
print(arr1)
print(arr2)




#....................MATRIX..............................

from numpy import *
m=matrix('1,2,3,4;5,6,7,8')
print(m)





#................................FUNCTIONS................................................
# def is used for functions..........
#we can call functions by variable name by number of times at any where

def a():
    print("hello world")
    print("good morning")
a()                 #here function is called by its variable

def add(x,y):
    print(x+y)      #print print the value here only it cannot be use to print to somewhere
add(5,6)         #here we passes two positional require arguments we dont pass the values it will shows an erro


def add(x,y):
    c=x+y
    return c      #return stores the values we can print it somewhere by using object
a=add(4,5)
print(a)

# calling two times a function........

def  a():
    print("hello world")
    print("good morning")

a()
print("byeeeeeeeeeeeeeeeeeee")
a()


#printing positional arugument some where
def a(x):
    print("hello",x)    #print the positional argument here
    print("what are u doing",x)      #number of times we use that arguments
a("user")
a("byeeeeee")

#example......
def a(x,y):
    result=x+y
    print(result)
a(4,5)
a("rgukt","rkv")

#example......
def update(x):
    x=8
    print(x)
a=10
update(a)
print(a)

#pass one list to another list in functios.............
def a(x):
    x[1]=10
    print(x)
b=[4,5,6]
a(b)
print(b)


# printing process by argument values..................
def a(name,age):
    print("hello",name)
    print("Age",age)
a("venki",17)        #it will take 1st item to first argument and 2nd to second argument
a(17,"venki")        #here also it take like above so it has no meaing less statement for user
a(age=17,name="venki")      #passing values by arguments name it will excute for that argument only



#by missing arument print default name....
def a(x="user"):
    print("hello",x)
a("venki")             #in this given item passes to argument
a()              #by missing the argument print default given value


#filter numbers by functios............
def even(x):
    return x%2==0
nums=[2,4,3,5,6,7,8,9]
evens=list(filter(even,nums))
print(evens)


#count the evens and odds in list by function...................

# def count(lst):
#     even=0
#     odd=0
#     for i in lst():
#         if i%2==0:
#             even=even+1
#         else:
#             odd=odd+1
# lst=[23,45,67,98,87,65,43,3,6,8]
# evens,odds=count(lst)
# print("Even:{} and odd:{}".format(evens,odds))



#.......................(*)by using operator we passes number arguments in functios..........

def a(a,*b):
    print(a)
    print(b)
a(5,7,34,78,12)       #here 1 item passes 1st argument and other all items passes to next *argument


#for loop in functions...............
def a(*x):
    sum=0
    for i in x:
        sum=sum+i
    print(sum)
    print(x[2])
a(2,3,5,7,9,45,56)



#return in for loop functions.......................
def add(*nums):
    result=0
    for x in nums:
        result=result+x
    return result
sum=add(3,6,7,9)
print(sum)

#output is in tuple form normally
def person(*data):
    print(data)
person("venki",56,"rgukt")




#...................(**) arbitary keyword arguments.........................
#it is in dictionary mapping form to given both key name and key value this will be used

def person(**data):
    print(data)
person(name="venki",age=17,collage="rgukt")


#printing form by one by one below..............
def person(**data):
    for k,v in data.items():
        print(k,":",v)
person(name="venki",age=17,collage="rgukt")




#.....................LOCAL VARIABLES AND GLOBAL VARIABLES..................
#global variable means its a variable it can execute at any where  ,like inbetween functions other
#local avariable is a variable it excute   in the diffeining function only.

a=10              #global variable
def great():
    a=15            #local variable
    print("inside",a)
great()
print("out",a)


#GLOBAL VARIABLE in local scope and global scope location.........

a=100     # global variable
def great():
    print("in",a)        #global variable in local scope
great()
print("out",a)         #global variable in global scope



#LOCAL VARIABLE IN local and global scope position..........

def great():
    z=9        #local variable
    print("in",z)       #local scope
great()
#print("out",z)   #it is global scope their no global variabe we run its show an error



# changing global and local scope value in  by using local variable......

a=101           #global variable
def great():
    global a
    a=90   #local variable
    print("inside",a)      #local scope
great()
print("outside",a)    #global scope


#changing global variable value only by using local variable position........

a=2
def great():
    a=9
    print("inside",a)
    globals()["a"]=15    #for changing global variable value
great()
print("outside",a)




#........................FIBONACCI SEQUENCE.................................

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
fib(5)
fib(1)
print("completed fibonacci sequence")




#............................FACTORIAL FOR A GIVEN NUMBER........................................
#by function method...
def fac(n):
    f=1           #intialise f value
    for i in range(1,n+1):
        f=f*i
    return f        #return f to print by an object......
x=5
result=fac(x)
print(result)

#normal for loop....
n=5
f=1
for i in range(1,n+1):
    f=f*i
print(f)




#................................RECURSSION.............................

# def great():
#     print("hello")
#     great()   #it will give an error becuse it recurring nearly 1000s of times
# great()

#to know recursion limit
import sys
print(sys.getrecursionlimit())

#to set recursion limit.............
import sys
sys.setrecursionlimit(200)
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
print(fact(10))



#...........................LAMBDA....................................................
#using multiple statements in single line we use lambda

x=lambda a,b:a+b
y=lambda a,b:a*b
print(x(5,6))
print(y(5,6))




#............................... FILTER, MAP ,REDUCE............................................
#filter
def is_even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8,96,58,33]
evens=list(filter(is_even,nums))   #filter even numbers from the list
print(evens)

nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))    #filter by lambda
print(evens)

#map.......................
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))        #map to to doubles the values..
print(evens)
print(doubles)

#reduce.................

from functools import reduce
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))      #filter evens here
doubles=list(map(lambda n:n*2,evens))             #by using map we double the values here
sum=reduce(lambda a,b:a+b,doubles)         #we add all numbers here reduce the lsit
print(evens)
print(doubles)
print(sum)




#...............................DECORATERS..............................................................
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



# ...........................(__NAME__) .................................
#we use __name__ variable in the file its  result is __main__
#we import file to another file ,__name__ use in  importing file its result file name

print(__name__)           #its main

import python2         #this from import its result file name instead of __name__
print(__name__)              #this is main file__name__

import python2           #here we import python 2 file their is code in function a() variable it is not showned gere because of that code is only for that main file only
#that code is

#code for main file only it will be not run by importing
def a():
    print("hello")
if __name__== "__main__":
    a()




#.....................CLASS AND OBJECTS..........................................................

class computer():
    def config(self):
        print("hello user whats happen")
a=computer()
a.config()

#special __init__ method
class computer:
    def __init__(self):    #__init__ method..it will be execute without calling function its default
        print("hello user this is init method....")
a=computer()


#............................DIFFERENT TYPES OF VARIABLES...............

class computer:
    charger=1                    #static /class variables   this value is same every where we can change it can change for all functions
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


#changing the values ....

class car:
    def __init__(self):
        self.mil=10
        self.com="benz"
c1=car()
c2=car()
c1.mil=20
print(c1.com,c1.mil)
print(c2.com,c2.mil)


class car:
    wheels=4               #static variable............
    def __init__(self):
        self.mil=10
        self.com="bmw"
c1=car()
c2=car()
c1.mil=20               #changing instant variable value
car.wheels=8                    #staric variable call by class name
print(c1.com,c1.mil,car.wheels)
print(c2.com,c2.mil,car.wheels)



#inner classs(class inside a class................................

class student:                 #outer classs
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()   #here inner class call to outer class
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()               #here we call inner class function
    class laptop:                       #inner class.....
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


#......................INHERITANCE  ....................................

class A:              #super classs.........
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
            print("feature 2 is working")

class B:      #sub classs..............................
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


#three classes.........
class A:             #grnad parent class.............................
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
            print("feature 2 is working")

class B(A):     #we inheritance a in b    #parent classsss........................
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

class C(B):         #child class                  #we written like C(A,B)  for inhertance both
    def feature5(self):
        print("feature 5 is working")
    def feature6(self):
        print("feature 6 is working")

c1=C()
c1.feature1()
c1.feature3()
c1.feature6()




#..........CONSTRUCTORS.........................................

class A:
    def __init__(self):               #this is constructor.......
        print("from A init")
    def fig1(self):
        print("figure 1 is flower")
class B(A):        # there is no constructor in B class so it will call A constructor.....
        def fig2(self):
            print("figure 2 is fruit")
b1=B()                      #we just call only class here not functions

print("code completed")

# A constructor not showned below by calling B child classss...........
class A:
    def __init__(self):            #  A  constructor
        print("from A init")
    def fig1(self):
        print("figure 1 is flower")
class B(A):
    def __init__(self):        #  B  constructor
        print("from B init")
    def fig2(self):
        print("figure 2 is fruit")
b1=B()                            #call class only...

print("code completed")

#print child and parent class constructors by this code......................

class A:
    def __init__(self):
        print("from A init")
    def fig1(self):
        print("figure 1 is flower")
class B(A):
    def __init__(self):
        super().__init__()           #for calling parent class constructor also..
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





###..............POLYMORPHISM..........................................
#.........DUCK TYPING.............................

class pycharm:
    def execute(self):
        print("duck typing is simple")
        print("santoor is a soap")

class laptop:
    def code(self,ide):
        ide.execute()       #here above class function we call
i =pycharm()
lap1=laptop()
lap1.code(i)       #1st class passes to second class function


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


#............OPERATOR OVERLOADING............................................
a=5
b=6
print(type(a))
print(a+b)
print(int.__add__(a,b))      #this is the process what happening inside a code
print(int.__sub__(a,b))


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


#.............................METHOD OVERLOADING....................................................

class student:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:       #if we pass three parameters
            s=a+b+c
        elif a!=None and b!=None:         #if we pass two parameters
            s=a+b
        else:                    #pass one parameter
            s=a
        return s
s1=student()
print(s1.sum(5))
print(s1.sum(2,3,4))
print(s1.sum(2,4))



#..................METHOD OVERIDDING......................................................
class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):            #here we rewrite the class A funtion value in class B function
        print("in B show")
a1=B()
a1.show()



#..................ITERATORS...............................................................

nums=[7,8,9,5]
it=iter(nums)
print(it)           #it will info of it
print(it.__next__())                #__next__ is used to print the next value
print(it.__next__())
print(it.__next__())
print(it.__next__())
print("iterate completed by using net its time for forloop")
for i in nums:
    print(i)


class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):       #this is iterating function
        return self
    def __next__(self):
        val=self.num
        self.num+=1
        return val
values=topten()
print(values)       #it will gives info
print(values.__next__())       #we use 1 __next__ it will give 1 st value only
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
for i in values:
    print(i)



#............GENERATORS.....................................................

def topten():
    yield 5           #yield also like return and print
values=topten()
print(values)             #show info
print(values.__next__())


def topten():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
values=topten()
print(values)                    #shows info....
for i in values:
    print(i)

#......printing the square roots .................

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



#................EXCEPTION HANDLING...............................................

a=5
b=2
print(a/b)

#if any error ocurring instead of error we print a statement
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
    print("resource close")      #it will not print because condition not run so it skip to exception part
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
    print("resource close")                         #here condition is true so it cant come to exception part


#print resource close also.....................
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
b=2    # we can change the value for another output
try:
    print("resource opened")
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


#.................MULTI THREADING............................

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
            sleep(1)
class hi(Thread):
    def run(self):
        for i in range(2):
            print("hi")
            sleep(1)
t1=hello()
t2=hi()
sleep(0.2)
t1.start()                #instead of run we use start its default in python
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
t1.join()              #these are used for printing the below print statement after completion of loop
t2.join()
print("bye")



#........................FILE HANDLING.........................................

a=open("mydata","r")              #r is for only reading the file
print(a.read())

a=open("mydata","r")
print(a.readline())               #to print first line in file

f=open("abc","w")                 #w for wrinting the file if their is no file it will create new file
f.write("laptop")
f=open("abc","a")               #a is append the value to the file
f.write("hello guys whats going onnn......")
f.write("neekenduku raaaaaaaaaaa")
f.write("have a drink")
f=open("abc","r")
print(f.read())

#to write data from one file to another file
f=open("mydata","r")
f1=open("ab","a")       #we use w  we write, it will not able to print because we just write it will remove after next statement #check in ab file
for data in f:
    f1.write(data)

c=open("ab","r")
print(c.read())

c=open("ab","r")
print(c.readline())

# f=open("images.png","rb")    #once run it.................
# for i in f:
#     print(i)

f=open("images.png","rb")      # check in location there are two images with different location........
f1=open("myimg","wb")          #rb for readand binary ............wb for write and bianry..
for i in f:
    f1.write(i)





#............LINEAR SEARCH.......................................

pos=-1                       #for starting from 0 use -1
def search(list,n):      #n is searching value list
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
    print("value Found at",pos)
else:
    print("value not found")


pos=-1
def search(list,n):      #n is searching value list
    i=0
    while i<len(list):
        if list[i]==n:
            globals()["pos"]=i
            return True
        i=i+1
    return False
list=[5,8,4,6,9,2]
n=10
if search(list,n):
    print("Found at",pos)
else:
    print("not found")





#..............................BINARY SEARCHING...............................................................


pos=-1               #for starting from 0 use -1
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
n=98
if search(list,n):
    print("found at",pos)
else:
    print("not found")



#...................BUBBLE SORTING.....................................................

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                print(nums)
nums=[5,3,4,8,6]
sort(nums)
print(nums)



#.....................SELECTION SORTING...........................................................

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




#......................DATE AND TIME....................

#gives date and time
import datetime
a=datetime.datetime.now()
print(a)

import datetime as dt
a=dt.datetime.now()
print(a)
print(a.year)


import datetime as dt
pt=dt.datetime.now()
f1=pt.strftime("%d-%m-%y,%A")
print(f1)














































