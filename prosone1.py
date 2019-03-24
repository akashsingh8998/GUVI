# your code goes here
N=int(input())
a=[]
b=[]
for i in range(N):
    x=list(input())
    a.append(x)
m=len(a[0])
N=a[0]

for i in range(1,len(a)):
    if m<len(a[i]):
        m=m
    else:
        m=len(a[i])
        N=a[i]

for i in range(m):
    k=j=0
    while k<len(a):
        if N[i]!=a[k][i]:
            j=-1
            break
        else:
            j=1
            k=k+1
    if j==1:
        b.append(N[i])
    elif j==-1:
        break
str=""
b=str.join(b)
print(b)
