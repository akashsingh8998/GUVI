mm,kk = input().split()
kk = int(kk)
b = False
l = list(map(int,input().split()))
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j] == kk:
            b = True
print("yes" if b else "no") 
