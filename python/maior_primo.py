def is_primo(y):
    count = 2
    while count < y:
        if y % (count - 1) == 0:
            return False
        count += 1
    return True

def maior_primo(x):
    if x < 2:
        return

    while x > 2:
        div = 0
        count = 3
        while count <= x:
            if is_primo(x):
                div += 1
            count += 1
        if div == 0:
            return x
        x -= 1

maior_primo(100)