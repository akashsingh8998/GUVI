# your code goes here
n, k = map(int, input().split())

a = []

for _ in range(n):
    b = set(map(int, input().split()))
    a.append(b)

t = set.intersection(*a)

print(*t)
