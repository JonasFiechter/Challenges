def vowels(x):
    printa(x)
    return True if x.lower() in ['a', 'e', 'i', 'o', 'u'] else False

    
print(vowels('I')) # CHAMANDO A FUNCAO VOWELS AQUI

def printa(y):
    print(f'ESSE É O Y: {y}')