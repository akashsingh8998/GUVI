# your code goes here
n,k = input().split()
n,k = int(n),int(k)
a = list(map(int,input().split()))
a = set(a)
a = list(a)
a = sorted(a)
print(a[-k])
