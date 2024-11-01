a = input()

sum = 10 
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        sum += 5
    else: 
        sum += 10

print(sum)