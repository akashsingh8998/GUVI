# your code goes here
N = int(input())
flag = 0
if(N>1):
	for i in range (2,N):
		if(N%i == 0):
			flag = 1
	if(flag == 1):
		print("no")
	else:
		print("yes")
else:
	print("no")
