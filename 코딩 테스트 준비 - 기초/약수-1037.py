import math
from functools import reduce

a = int(input())
arr = list(map(int, input().split()))
arr2 = reduce(math.gcd, arr)
arr3 = reduce(math.lcm, arr)

print(arr2 * arr3)