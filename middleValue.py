# To find the mid value
def another():
    li1 =[3,1]
    li2 =[1,1]
    li=li1+li2
    size=len(li)
    if(size%2==0):
        m=size//2
        print((li[m]+li[m-1])/2)
    else:
        print(li[m])

another()