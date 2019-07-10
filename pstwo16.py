from collections import Counter
n=int(input())
x = input().split()
y=Counter(x)
print(min(y,key=y.get))
