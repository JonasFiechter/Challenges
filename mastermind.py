'''
Mastermind
The classic game of Mastermind is played on a tray on which the Mastermind 
conceals a code and the Guesser has 10 tries to guess it. The code is a 
sequence of 4 (or 6, sometimes more) pegs of different colors. Each guess is a 
corresponding sequence of 4 (or more) pegs of different colors. A guess is 
"correct" when the color of every peg in the guess exactly matches the 
corresponding peg in the Mastermind's code.

After each guess by the Guesser, the Mastermind will give a score comprising 
black & white pegs, not arranged in any order:

Black peg == guess peg matches the color of a code peg in the same position.
White peg == guess peg matches the color of a code peg in another position.
Create a function that takes two strings, code and guess as arguments, and 
returns the score in a dictionary.

The code and guess are strings of numeric digits
The color of the pegs are represented by numeric digits
no "peg" may be double-scored
Examples
guess_score("1423", "5678") ➞ {"black": 0, "white": 0}

guess_score("1423", "2222") ➞ {"black": 1, "white": 0}

guess_score("1423", "1234") ➞ {"black": 1, "white": 3}

guess_score("1423", "2211") ➞ {"black": 0, "white": 2}
Notes
The code and guess sequences will have the same length.
The "pegs" consists of only digits from 0-9.
'''

# solution 1
def guess_score(guess, code):
    results = {
        'black': 0,
        'white': 0
    }
    
    for index, item in enumerate(guess):
        if item == code[index]:
            results["black"] += 1
        elif item in code:
            results["white"] += 1

    return results

print(guess_score("1423", "5678"))
print(guess_score("1423", "2222"))
print(guess_score("1423", "1234"))
print(guess_score("1423", "2211"))