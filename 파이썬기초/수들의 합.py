a = int(input())
sum = 0
b = 1
n = 0

while sum + b <= a:
    sum += b
    b += 1
    n += 1

print(n)