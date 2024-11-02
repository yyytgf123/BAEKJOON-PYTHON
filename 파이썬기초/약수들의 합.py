while 1:
    a = int(input())    
    sum = 0
    list = []
    
    if a == -1:
        break

    for i in range(1, a):
        if a % i == 0:
            sum += i
            list.append(i)

    factor = ' + '.join(map(str, list))

    if sum == a:
        print(f"{a} = {factor}")
    elif sum != a:
        print(f"{a} is NOT perfect.")

    list.clear()
    factor = ""
