# your code goes here
n,m = input().split()
n = int(n)
m = int(m)
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if(set(b) <= set(a)):
	print("YES")
else:
	print("NO")
