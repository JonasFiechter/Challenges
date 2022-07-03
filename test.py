def multiples(number, max):
    for n in range(max):
        if (n + 1) >= number and (n + 1) % number == 0:
            print(n + 1, end=' ')

multiples(4, 100)