a,b,c = map(int, input().split())
if a == b == c:
    print(int(10000 + a * 1000))
elif a == b or b == c or c == a:
    same = a if a == b or a == c else b
    print(int(1000 + same * 100))
else:
    print(max(a,b,c) * 100)
