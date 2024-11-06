a, b = map(int, input().split())
c = list(map(int, input().split()))
count = 0

start = 0
current_sum = 0

for i in range(a):
    current_sum += c[i]

    while current_sum > b:
        current_sum -= c[start]
        start += 1
    
    if current_sum == b:
        count += 1
    
print(count)