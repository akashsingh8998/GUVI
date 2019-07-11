# your code goes here
import math
n = int(input())
a = []
while(n % 2 == 0): 
	a.append(str(2))
	n = n / 2

for i in range(3,int(math.sqrt(n))+1,2):
	while(n % i == 0):
		a.append(str(i))
		n = n / i
if(n > 2): 
	a.append(str(n))
a = list(set(a))
print(" ".join(a))
