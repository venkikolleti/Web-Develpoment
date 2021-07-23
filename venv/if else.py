# a=int(input("enter a num:"))
# b=int(input("enter b num:"))
# c=int(input("enter c num:"))
# if a<b:
#     if a<c:
#         print("a is greater")
#     else:
#         print("c is greater",c)
# else:
#     if b<c:
#         print("b is greater")
#     else:
#         print("c is greater")
#
# a=5
# b=7
# c=a
# a=b
# b=c
# print(a,b)
a=int(input("enter a num:"))

a,b=input("enter numbers").split()
a=int(a)
b=int(b)
c=a*b
print(c)



a,b,c=input("enter a num:").split()
a=int(a)
b=int(b)
c=int(c)
if(a<=b and a<=c):
    print ("a is minimum")
elif b<=a and b<=c:
    print("b is minimum")
else:
    print("c is minimum")

a=open("while.py","r")
print(a)

