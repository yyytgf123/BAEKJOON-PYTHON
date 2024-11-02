a = int(input())

for i in range(a):
    b = input()
    sum = 0
    count = 0

    for j in b:
        if j == "O":
            sum += 1
            count += sum
        else:
            sum = 0
    print(count)