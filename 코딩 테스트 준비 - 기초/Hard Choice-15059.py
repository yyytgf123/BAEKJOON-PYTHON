a,b,c= map(int, input().split())
d,e,f = map(int, input().split())
sum1 = 0
sum2 = 0
sum3 = 0

if a < d:
    sum1 = d - a

if b < e:
    sum2 = e - b

if c < f:
    sum3 = f - c

print(sum1)
print(sum2)
print(sum3)
print(sum1+sum2+sum3)