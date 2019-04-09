# your code goes here
n = int(input())
a = []
b = input().split()
for i in range(0,n):
	a.append(int(b[i]))

d = []

for i in range(0,n):
	if (i%2==0) and (a[i]%2==1):
		d.append(str(a[i]))
	elif (i%2==1) and (a[i]%2==0):
		d.append(str(a[i]))
print(" ".join(d))
		
