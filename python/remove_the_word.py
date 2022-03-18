'''
Create a function that takes a list and string. The function should remove the letters in the 
string from the list, and return the list.
'''


def remove_word(list_, word):

    for letter in word:
        for n, letter2 in enumerate(list_):
            if letter == letter2:
                list_.pop(n)
                break

    return list_


if __name__ == '__main__':
    print(remove_word(['m', 'v', 'f', 'a', 'b', 'a', 'c', 'm', 'a', 'r', 'o', 'x'], 'marco'))