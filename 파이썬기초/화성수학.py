a = int(input())

for i in range(a):
    b = input().split()
    result = float(b[0])

    for j in b[1:]:
        if j == '@':
            result *= 3
        elif j == '%':
            result += 5
        elif j == '#':
            result -= 7

    print(f"{result:.2f}")