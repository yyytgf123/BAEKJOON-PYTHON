year = int(input())

leap_year = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
    else:
        leap_year = True

if leap_year:
    print("1")
else:
    print("0")