def num(*i):
    Sum=0
    for x in i:
        Sum=Sum+x
    # print(Sum)
# num(2,3,4,5,6,6,8,5,3,5,7)

# a={"name":"venki","sname":"kolleti"}
#print(a)
def person(data):
    print(" ")
    hkl=0
    for kl,hl in data.items():
        if hkl<len(kl):
            hkl=len(kl)
    for k,v in data.items():
        if hkl ==len(k):
            print(k,' :',v)
        else:
            space=' '
            balance_ln=hkl-len(k)
            for x in range(balance_ln):
                space+=' '
            print(k+space,':',v)
userdata={}
e=1
while e !='0':
    userkey=input("enter key:")
    uservalue = input("enter value:")
    userdata[userkey]=uservalue
    e=input("enter 0 to end or any key to continue adding...")
person(userdata)