'''
Recursion: Count The Digits
Create a function that will recursively count the number of digits of a number. 
Conversion of the number to a string is not allowed, thus, the approach is 
recursive.

Examples
digits_count(4666) ➞ 4

digits_count(544) ➞ 3

digits_count(121317) ➞ 6

digits_count(0) ➞ 1

digits_count(12345) ➞ 5

digits_count(1289396387328) ➞ 13
Notes
All inputs are integers but some are in exponential form, deal with it 
accordingly.
You are expected to come up with a solution using the concept of recursion or 
the so-called recursive approach.
Check out the Resources for more topics about recursion to read on 
(if you aren't familiar with it yet or haven't fully understood the concept 
behind it before taking up this challenge or unless otherwise).
An iterative version of this challenge can be found via this link.
'''

def digits_count(entry_number, count=1):
    # print(entry_number)
    if entry_number < 0:
        entry_number *= -1
    if entry_number // 10 != 0:
        count += 1
        entry_number = entry_number // 10
        return digits_count(entry_number=entry_number, count=count)

    return count

if __name__ == '__main__':
    testing = [ 
        0, 4666, 544, 121317, 12345, 1289396387328, -1232323, 3463463874638476, 
        -231.2e6, 1283939312321, -231273683, 3.2e6, 314890e3 
    ]
    for v in testing:
        print(digits_count(v))
