n = int(input())

# 소인수분해
factor = 2
while n > 1:
    if n % factor == 0:
        print(factor)
        n //= factor
    else:
        factor += 1
