# 모두 값 입력 후 값 출력
a = int(input())

for _ in range(a):
    yonsei_score = 0
    korea_score = 0

    for _ in range(9):
        b, c = map(int, input().split())
        yonsei_score += b
        korea_score += c

    if yonsei_score > korea_score:
        print("Yonsei")
    elif korea_score > yonsei_score:
        print("Korea")
    else:
        print("Draw")
#-----------------------------------------
# 나머지 횟수는 0 0으로 채움
a = int(input())

for i in range(9):
    base = 0
    base2 = 0
    for j in range(a):
        b, c = map(int, input().split())
        if b > c:
            print("Yonsei")
        elif b < c:
            print("Korea")
        elif b == c:
            print("Draw")

    print(("0 0\n" * (9 - a)).strip())
    break