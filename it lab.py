# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# c=a*b
# print(c)
#
# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# a,b=b,a
# print("swap of a:",a)
# print("swap of b:",b)
"""
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
print(min(a,b,c))

a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a<b:
    if a<c:
        print("a is minimum:",a)
    else:
        print("c is minimum:",c)
elif b<a:
    if b<c:
        print("b is minimum:",b)
    else:
        print("c is minimum:",c)

else:
    print("c is minimum:",c)

n=int(input("enter a number:"))
s=0
i=1
while (i<=n):
    print(i)
    s=s+i
    i=i+1
print(s)


n=10
i=1
while n>=i:
    print(n)
    n=n-1"""


n=10
i=1
s=0
while(i<=n):
    if n%i==0:
        print(i)
        s=s+1
    i=i+1
print("count the number of factors:",s)

n=6
i=1
s=1
while(i<=n):
    print(i)
    s=s*i
    i=i+1

print("count the number of factors:",s)

message=input("enter any uppercase letters:")
LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for key in range(len(LETTERS)):
    translated=''
    for symbol in message:
        if symbol in LETTERS:
            num=LETTERS.find(symbol)
            num=num-key
            if num<0:
                num=num+len(LETTERS)
            translated=translated+LETTERS[num]
        else:
            translated=translated+symbol
print(translated)

shift=-1
text="HBEGRRJ"
encryption=""
for a in text:
    if a.isupper():
        a_unicode=ord(a)
        a_index=ord(a)-ord("A")
        new_index=(a_index+shift)%26
        new_unicode=new_index+ord("A")
        new_character=chr(new_unicode)
        encryption=encryption+new_character
    else:
        encryption+=a
print("plain text:",text)
print("encrypted text:",encryption)



# n=input("enter a value:")
# a=list(map(str,input().split()))
# m=[]
# for i in a:
#     if i not in m:
#         m.append(i)
# print("".join(m))

# from array import *
# n=input("length of array:")
# a=array([input("enter values with space:").split()])
# b=int(a)
# m=[]
# for i in b:
#     if i not in m:
#         m.append(i)
# print("".join(m))


from array import *
arr=array("i",[])
n=int(input(("length of array:")))
x=input("enter the values :").split()
for i in x:
    z=int(i)
    if z not in arr:
        arr.append(z)
print(arr)




# from array import *
# arr=array("i",[])
# n=int(input("enter the length of the array:"))
# for i in range(n):
#     x=input("enter the next value").split()
#     arr.append(x)
# print(arr)


message=list(map(str,input("enter the message:")))
decode_message=[]
for i in message:
    decode_letter=((ord(i)-3+65)%26)+65
    decode_message.append(chr(decode_letter))
decode_message=("".join(reversed(decode_message)))
print(decode_message)


n=int(input("enter"))
s=input("enter num:").split()
if len(s)!=n:
    exit()
l=list()
for i in s:
    x=int(i)
    if x not in l:
        l.append(x)
    print(x," ",end="")

n=int(input("enter"))
s=input("enter num:").split()
if len(s)!=n:
    exit()
x=list()
for i in s:
    x.append(int(i))
l=list()
for i in x:
    if i not in l:
        l.append(i)
        print(i," ",end="")


s=input("enter")
x=s[::-1]
r=""
for i in x:
    r+=chr((ord(i)-65-3)%26+65)
print(r)