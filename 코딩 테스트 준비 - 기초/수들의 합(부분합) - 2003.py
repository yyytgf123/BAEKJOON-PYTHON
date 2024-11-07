a, b = map(int, input().split())
c = list(map(int, input().split()))
count = 0

start = 0
current_sum = 0

for i in range(a):
    current_sum += c[i]
    # list의 숫자를 하나씩 대입해서 b보다 큰 값으로 만드는 과정

    while current_sum > b:
        current_sum -= c[start]
        start += 1
    # current_sum보다 크면 list c에서 값을 앞에서 가져와 빼주고 if문으로 이동
    # 1. 작아지면 while문에서 빠져나옴
    # 2. 같아지면 if문 조건에 맞게 count +1 해줌

    if current_sum == b:
        count += 1

print(count)