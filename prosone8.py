# your code goes here
def gcd(k,r):
    for i in range(k-1,r):
        g.append(int(a[i]))
    g1=max(g)
    for j in range(1,g1+1):
        fl=0
        for k in range(len(g)):
            if g[k]%j!=0:
                fl=1
        if fl==0:
            x=j
            
    print(x)

s=input().split()
n,q=int(s[0]),int(s[1])
b1,a,g=[],[],[]
z=input().split()
for k in range(n):
    a.append(z[k])
for p in range(q):
    b=input().split()
    b1.append(b)
for u in  range(q):
    if b1[u][0]==b1[u][1]:
        f=int(b1[u][0])
        print(a[f-1])
    else:
        k=int(b1[u][0])
        r=int(b1[u][1])
        gcd(k,r)
