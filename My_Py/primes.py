def primes():
    n = 2
    flag = True
    while True:
        if flag:
            yield n
        n += 1
        flag = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                flag = False
                break
