# your code goes here
m, n = [int(i) for i in input().split()]
z = [i for i in input().split()]
z = ''.join(z) 
for i in range(n):
    z = z[len(z)-1]+z[0:len(z)-1]
print(' '.join(z))
