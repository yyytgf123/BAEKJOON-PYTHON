num = int(input())

if num % 10 == 0:
    A = (num //300) % 300
    num2 = num % 300
    B = (num2 // 60) % 60
    num3 = num % 60
    C = (num3 % 60) // 10

    print(A, B, C)

elif num % 10 != 0:
    print("-1")
