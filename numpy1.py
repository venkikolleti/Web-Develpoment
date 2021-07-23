from numpy import *
arr=array([1,2,3,4,5])
print(arr)
print(arr.dtype)


from numpy import *
arr=array([1,2,3,4,5.2])
print(arr)



from numpy import *
arr=array([1,2,3,4,5.2],int)
print(arr)


from numpy import *
arr=linspace(0,5,6)
print(arr)


from numpy import *
arr=linspace(0,5,10)
print(arr)


from numpy import *
arr=arange(1,15,2)
print(arr)


from numpy import *
arr=logspace(1,40,5)
print(arr)
print(arr[0])



from numpy import *
arr=zeros(5)
print(arr)


from numpy import *
arr=ones(5)
print(arr)


from numpy import *
arr=array([1,2,3,4,5])
arr=arr+5
print(arr)


from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([4,8,9,3,6])
arr=arr1+arr2
print(arr)


from numpy import *
arr1=array([1,2,3,4,5,45])
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))

