a=1
print(a)
print("hello world")
a=[1,2,3,4]
a.extend([5,6,7])
print(a)
a={1:3,2:4,5:6}
a.popitem()
print(a)
a.popitem()
print(a)

marks=30
if marks >=35:
    print("you passed")
else:
    print("you failed")

marks=70
if marks ==35:
    print("you passed")
elif marks>35:
    print("you promted")
else:
    print("you failed")

marks=79
if marks ==35:
    print("you passed")

elif marks>35:
    print("you promted")
    if marks>75:
        print("you got good marks")
else:
    print("you failed")


from example import add
import platform
print(add(2,3))
print(platform.system())

