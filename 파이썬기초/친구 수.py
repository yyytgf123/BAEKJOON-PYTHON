sum = 0

while True:
    a,b = map(int, input().split())
    
    if a == b == 0:
        break

    sum = a + b
    print(sum)