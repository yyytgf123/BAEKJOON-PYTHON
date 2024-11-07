from itertools import combinations

a = [int(input()) for i in range(9)]

for combintion in combinations(a, 7):
    if sum(combintion) == 100:
        result = sorted(combintion)
        for j in result:
            print(j)
        break