n=100
i=1
s=0
while(i<=n):
    s=s+i
    i=i+1
print("Sum is:",s )


sum=0
for i in range(1,101):
    sum=sum+i
print("sumation is:",sum)

i=1
while(i<=100):
    print(i)
    i=i+1

s=0
for i in range(1,101,2):
    print(i)
    s=s+i
print(s)


n=5
for x in range(1,n+1):
    for y in range(1, n + 1):
        if((y==1 or y==n)or (x==1 or x==n)):
            print("  *",end="")
        else:
            print("",end="")

    print("")
# a=int(input("enter a value:"))
# b=int(input("enter b value:"))
# c=int(input("enter c value:"))
# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# elif b>a:
#     if b>c:
#         print("b is greatest")
#     else:
#         print("c is greatest")
#
# else:
#     print("c is greatest")
#
# n=int(input("enter a number:"))
# i=2
# while(i<n):
#     if(n%i==0):
#         print("it is not a prime")
#         break
#     i = i + 1
# else:
#     print("it is prime")
#
# n=int(input("enter a number:"))
# for i in range(2,n):
#     if(n%i==0):
#         print("not a prime")
#         break
# else:
#     print("it is prime")
#
#
# n=input("enter a number:")
# print(n[0])
# print(n[-1])
# a="a"
# print(ord(a))
b=ord("A")
print(b)
for i in range(97,123):
    print(chr(i))
for i in range(64,91):
    print(chr(i))

i=97
while(i<=122):
    print(chr(i))
    i=i+1

i=64
while(i<=90):
    print(chr(i))
    i=i+1

a=10
b=20
x=a
a=b
b=x
print("swaap of a:",a)
print("swap of b:",b)
a=20
b=30
a,b=b,a
print("swap a:",a)
print("swap b:",b)



n=int(input("enter anumber"))
i=5
while(i<=n):
    print("heloo")
    i=i+1