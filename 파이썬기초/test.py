import math

# 입력 받기
A, I = map(int, input().split())

# 저작권이 있는 멜로디의 최소 개수 계산
B = (I - 1) * A + 1

print(B)
