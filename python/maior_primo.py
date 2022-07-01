#  Solution 1
def maior_primo(x):
    if x < 2:
        return

    while x > 2:
        div = 0
        count = 3
        while count <= x:
            if x % (count - 1) == 0:
                div += 1
            count += 1
        if div == 0:
            return x
        x -= 1

#  Solution 2
def e_primo(y):
    count = y - 1
    while count >= 2:
        print(f'e_primo => {y} % {count} = {y % count}')
        if y % count == 0:
            return False
        count -= 1
    print(f'{y} é primo')
    return True

def maior_primo_2(x):
    while x >= 2:
        print(f'x => {x}')
        if e_primo(x):
            return x
        x -= 1


#  Solution 3
def maior_primo_3(x):
    for number in range(x, 1, -1):
        for number_comparative in range(number -1, 1, -1):
            if number % number_comparative == 0:
                break
            if number_comparative == 2:
                return number


print(maior_primo_3(20))