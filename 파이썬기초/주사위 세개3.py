num = int(input())

board1 = 100
board2 = 100

for i in range(num):
    a, b = map(int, input().split())
    if a > b:
        board2 -= a
    elif a < b:
        board1 -= b

print(f"{board1}\n{board2}")