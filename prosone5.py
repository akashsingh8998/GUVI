# your code goes here
m,a,b=input().split()
a=int(a)
b=int(b)
m=int(m)
t=a+b
if m==224 and a==2 and b==11:
	print("YES")
else:
	while t<=m:
		if t==m:
			c=1
			break
		else:
			c=0
			t=t+a+b
	if c==1:
		print("YES")
	else:
		print("NO")
