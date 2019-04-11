# your code goes here
n,k = input().split()
n,k = int(n),int(k)
a = input().split()
a = set(a)
a = list(a)
a = sorted(a)
print(a)
print(a[-k])
