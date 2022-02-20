from time import time

def calc_time(n1, n2):
    t1 = time()
    for i in range(1000):
        result = n1 * n2 + (n1 ** 50) - (n2 ** 50)
        result += n2 - 50 * (n1 / n2 ** 20)
        t2 = time() - t1
        print(f'Count: {i}, result: {result}, time count: {t2}')
    t3 = time() - t1
    print(f'{t3:.3f} seconds')

print(f'{calc_time(10, 10)}\nThis is the main calc with both numbers like 10')

if __name__ == '__main__':
    run = True
    while run:
        n1 = int(input('Place a number to be n1: '))
        n2 = int(input('And another to be n2: '))
        input('to exit place 0 for both numbers, press any key to continue...')
        calc_time(n1, n2)

        if n1 == 0 and n2 == 0 or n1:
            run = False