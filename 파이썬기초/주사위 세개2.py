a = int(input())

max_sum = 0
for i in range(a):
    b,c,d = map(int, input().split())

    if b == c == d:
        sum = 10000 + (b * 1000)
    elif b == c or c == d or d == b:
        list = [b,c,d]
        min_list = max(list, key=list.count)

        sum = 1000 + (min_list * 100)
    else:
        sum =  max(b,c,d) * 100

    max_sum = max(max_sum, sum)

print(max_sum)