# your code goes here
m,n=list(map(int,input().split()))
t=[[abs(i-n),i] for i in list(map(int,input().split(" ")))]
t.sort()
t=t[1:]
z=[i[1] for i in t[:3]]
print(*z)
