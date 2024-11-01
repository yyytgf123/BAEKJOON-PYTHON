a,b = map(int, input().split())
c,d = map(int, input().split())
e,f = map(int, input().split())

x = [a,c,e]
y = [b,d,f]

x_1 = min(x, key=x.count)
y_1 = min(y, key=y.count)

print(x_1, y_1)
