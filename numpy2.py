from numpy import *
a=array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a.flatten())


from numpy import *
a=matrix("1 2 3 4;5 6 7 8")
print(a)


from numpy import *
a=matrix("1 2 3; 4 5 6; 7 8 9")
print(a)
print(diagonal(a))
print(a.min())
print(a.max())


from numpy import *
a=matrix("1 2 3;4 5 6; 7 8 9")
b=matrix("9 8 7;6 5 4;3 2 1")
c=a+b
d=a*b
print(c)
print(d)




