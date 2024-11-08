E, S, M = map(int, input().split())

count = 0

while True:
    if(count - E) % 15 == 0 and(count - S) % 28 == 0 and(count - M) % 19 == 0:
        print(count)
        break
    count += 1