i = int(input('digite um numero: '))
x = 0

while i > 0:
    x = x + i % 10
    i = i // 10

print(x)
    