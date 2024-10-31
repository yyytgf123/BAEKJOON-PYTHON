import math

a = int(input())

for i in range(a):
    b, c = map(int, input().split())
    lcm = math.lcm(b,c)
    print(lcm)