# your code goes here
l,r = [int(x) for x in input().split()]
g = max(l,r)
while(True):
	if(g%l==0 and g%r==0):
		lcm = g
		break
	g += 1
print(lcm)
