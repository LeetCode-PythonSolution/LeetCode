"""
Longest Substring Without Repeating Characters

"""
st=input()
li=[]
for i in range(len(st)):
    s=''
    for j in range(i,len(st)):
        if st[j] not in s:
            s+=st[j]
        else:
            break
    li+=[len(s)]
print(max(li))

