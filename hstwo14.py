# your code goes here
from itertools import permutations

n = input()

m = permutations(n)
m = list(dict.fromkeys(m))

for perm in m:
    print(''.join(perm))
