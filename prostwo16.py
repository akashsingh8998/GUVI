aa=int(input())
c=list(map(int,input().split()))
y=[1]*aa
for i in range(aa):
    if i==0:
        if c[i]>c[i+1]:
            y[i]=y[i]+y[i+1]
    elif i>0:
        if c[i]>c[i-1]:
            y[i]=y[i]+y[i-1]
print(sum(y))
