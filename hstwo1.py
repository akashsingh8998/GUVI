# your code goes here
a = input().split()
for i in range(0,len(a)):
	if (i<len(a)-1):
		b=" "
	else:
		b=""
	print(a[i][::-1],end=b)
