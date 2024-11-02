a = int(input())

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for i in range(a):
    b, c = map(int, input().split())
    if b > 0 and c > 0:
        count1 += 1
    elif b <0 and c < 0:
        count3 += 1
    elif b < 0 and c > 0:
        count2 += 1
    elif b > 0 and c < 0:
        count4 += 1
    else:
        count5 += 1

print(f"Q1: {count1}")
print(f"Q2: {count2}")
print(f"Q3: {count3}")
print(f"Q4: {count4}")
print(f"AXIS: {count5}")  