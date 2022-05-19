'''
The Hangman Game
Create a function that, given a phrase and a number of letters guessed, returns a string with 
hyphens - for every letter of the phrase not guessed, and each letter guessed in place.

Examples
hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"

hangman("tree", ["r", "t", "e"]) ➞ "tree"

hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"

hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"
Notes
The letters are always given in lowercase, but they should be returned in the same case as in 
the original phrase (see example #3).
All characters other than letters should always be returned (see example #4).
'''


def hangman(entry, letters_guessed):
    result = ''
    for l in entry:
        if l in letters_guessed or l in [l.upper() for l in letters_guessed]:
            result += l
        elif l == ' ':
            result += l
        else:
            result += '-'
    return result


if __name__ == '__main__':
    print(hangman("helicopter", ["o", "e", "s"]))
    print(hangman("Python rules", ["a", "n", "p", "r", "z"]))
    print(hangman("He's a very naughty boy!", ["e", "a", "y"]))