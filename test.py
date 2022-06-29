from time import sleep

n = int(input('digite o valor de n: '))

i = 0
count = 0

while count < n:
    print('DENTRO DE COUNT', count, i)
    sleep(1)
    if i % 2 != 0:
        print('DENTRO DO BLOCO IF IMPAR')
        print(i)
        count += 1
    i += 1