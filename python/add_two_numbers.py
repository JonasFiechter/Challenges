def add_two_numbers(l1: list, l2: list):
    l1_s = ''
    l2_s = ''

    for value in l1[::-1]:
        l1_s += str(value)

    for value in l2[::-1]:
        l2_s += str(value)

    result = int(l1_s) + int(l2_s)
    
    return [v for v in str(result)[::-1]]

a = ()
print(type(a))
a = (1,)
print(type(a))

l1, l2 = [2,4,3], [5,6,4]

print(add_two_numbers(l1, l2))