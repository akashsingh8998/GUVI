# your code goes here
n=int(input())
m=list(map(int,input().split()))
a=[]
for i in range(0,n-1):
  if m[i]>max(m[i+1:]):
    a.append(m[i])
a.append(m[n-1])
print(*a)
print(max(m))
