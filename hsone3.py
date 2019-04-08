# your code goes here
n = int(input())
a = []
b = input().split()
for i in range(0,n):
	a.append(int(b[i]))

c = []
for i in range(0,n):
	if(i == a[i]):
		c.append(str(a[i]))
if not c:
	print("-1")
else:
	c = sorted(c)
	print(" ".join(c))
