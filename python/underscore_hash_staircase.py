'''
Create a function that will build a staircase using the underscore _ and hash # 
symbols. A positive value denotes the staircase's upward direction and downwards 
for a negative value.

Examples
staircase(3) ➞ "__#\n_##\n###"
__#
_##
###

staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
______#
_____##
____###
___####
__#####
_######
#######

staircase(2) ➞ "_#\n##"
_#
##

staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
########
_#######
__######
___#####
____####
_____###
______##
_______#
'''

# Solution 1
def staircase(number):
    stairstring = ''
    level_count = (number - 1)
    if number > 0:
        for floor in range(number):
            stairstring += '\n'
            for n2 in range(number):
                if n2 >= level_count:
                    stairstring += '#'
                else: stairstring += '_'
            level_count -= 1
    
    else:
        number = number * (-1)
        level_count = (number * 1) + 1
        for floor in range(number):
            stairstring += '\n'
            for n2 in range(number, 0, -1):
                if n2 < level_count:
                    stairstring += '#'
                else: stairstring += '_'
            level_count -= 1
    
    return stairstring[1:]


# print(staircase(3))
# print(staircase(6))
# print(staircase(-6))

# Solution 2
def staircase2(steps_number):
    tick = steps_number
    result = ''
    for step in range(steps_number):
        result += (
            ''.join(['_' if (i + 1) < tick else '#' for i in range(steps_number)])
            ) + '\n'
        tick -= 1
    
    print(result)
    


staircase2(8)