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
    start = 1
    end = number + 1
    tick = 1
    steps = number 

    if number < 0:
        steps = number * (-1)
        tick = -1
        end = 0
        start = steps

    # if number > 0:
    for step_ in range(start, end, tick):
        # print(f'first {first_step}  last {last_step} number => {number}')
        stairstring += '\n'
        for n2 in range(steps):
            if n2 < steps - step_:
                stairstring += '_'
            else: stairstring += '#'

    return stairstring
    
    # else:
    #     number = number * (-1)
    #     level_count = (number * 1) + 1
    #     for floor in range(number):
    #         stairstring += '\n'
    #         for n2 in range(number, 0, -1):
    #             if n2 < level_count:
    #                 stairstring += '#'
    #             else: stairstring += '_'
    #         level_count -= 1
    
    


# print(staircase(3))
# print(staircase(6))
# print(staircase(-6))
staircase(5)