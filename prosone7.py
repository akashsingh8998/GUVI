y,z=1,2
t=int(input())
while z<=t:
    if 2**y==t:
        y=0
        break
    else:
        z=2**y
        y=y+1
if(y!=0):
    y=y-2
    a=t-2**y
    print(a)
else:
    print(0)
