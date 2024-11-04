n = int(input())
data = list(map(int, input().split()))
answer = 0

for x in data:
    cnt = 0
    if x == 1:
        continue
    else:
        for i in range(2, x + 1):
            if x % i == 0:
                cnt += 1
        if cnt == 1:
            answer += 1
            
print(answer)
