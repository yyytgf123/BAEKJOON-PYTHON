while True:
    try:
        n = int(input())
        if n == 0:
            break

        if n % 2 == 0 or n % 5 == 0:
            continue 

        remain = 1
        count = 1
        while remain % n != 0:
            remain = (remain * 10 + 1) % n
            count += 1

        print(count)
        
    except EOFError:
        break
