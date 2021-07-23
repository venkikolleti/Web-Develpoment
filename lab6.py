# from collections import *
# a=list(input("enter the num:").split())
# b=[]
# for i in a:
#     z=int(i)
#     b.append(z)
# print(b.count(b))

# h=["b","a","c","a","a","b","d"]
# c=[]
# n=3
# for i in h:
#     b=h.count(i)
#     c.append(b)
# print(c)
#
# # print(m)
# # for i in m:
# #     if i==n:
# #         print(i)
# #     else:
# #         print("not exist")
#
#
# a={"a":2,"b":3,"c":6}
# print(a["2])
#

# h=["b","a","c","a","a","b","d"]
# l=[]
# for i in h:
#     l[i]=h.count(i)
#
# print(l)




# def a(arr,n,k):
#     count_map={}
#     for i in range(0,n):
#         if arr[i] in count_map.keys():
#             count_map[arr[i]]+=1
#         else:
#             count_map[arr[i]]=1
#
#     for i in range(0,n):
#         if count_map[arr[i]]==k:
#             return arr[i]
#         i+=1
#
#     #return("integer not found")
# if __name__=="__main__":
#     arr=[1,7,4,3,4,8,7]
#     n=len(arr)
#     k=8
#     #print(a(arr,n,k))
#
#
#
#
#
#
#
# def a(arr,n,k):
#     count_map={}
#     for i in range(0,n):
#         if arr[i] in count_map.keys():
#             count_map[arr[i]]+=1
#         else:
#             count_map[arr[i]]=1
#
#     for i in range(0,n):
#         if count_map[arr[i]]==k:
#             return arr[i]
#
#
#     return("integer not found")
#
# d=input("enter the numbers:").split()
# arr=[]
# for i in d:
#     c=int(i)
#     arr.append(c)
# n=len(arr)
# k=int(input("enter value of k:"))
#
# print(a(arr,n,k))








s=input("enter the  numbers:")
k=int(input("enter the k value:"))
l=list()
for i in s.split():
    l.append(int(i))

for i in l:
    if l.count(i)==k:
        print(i)
        break
else:
    print("integer not found")




















