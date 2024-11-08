from itertools import combinations

a = [int(input()) for _ in range(9)]

for i in combinations(a, 7):
    if sum(i) == 100:
        result = sorted(i)
        for j in result:
            print(j)
        break
