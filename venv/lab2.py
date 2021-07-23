# n=int(input("enter the number of rows:"))
# num=1
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(i**2,end="")
#         #num=num+1
#     print()

# i=1
# while(i<=4):
#     j=1
#     while(j<=5):
#         print(j**2,end="")
#         j=j+1
#     i=i+1
#     print()




n=int(input("enter a number:"))
i=1
sum=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
    i=i+1
print(sum)



n=4
num=1
for i in range(0,n):
    for j in range(0,i+1):
        print(num**2," ",end="")
        num=num+1
    print(" ")


a=input("enter anything:")
b=input("enter something:")
if(sorted(a)==sorted(b)):
    print("the given string is anagram")
else:
    print("not a anagram")

class computer:
    def __init__(self):
        print("heloo")
a=computer()