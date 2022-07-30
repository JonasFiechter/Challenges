'''
Majority Vote
Create a function that returns the majority vote in a list. A majority vote is 
an element that occurs > N/2 times in a list (where N is the length of the list).

Examples
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
Notes
The frequency of the majority element must be strictly greater than 1/2.
If there is no majority element, return None.
If the list is empty, return None.
'''

#  Solution 1 (it doesn't solve the equal situations)
from numpy import equal
from pandas import options


def majority_vote(list_):
    list_of_options = []
    count_of_options = []

    #  Feeding options
    for i in list_:
        if i not in list_of_options:
            list_of_options.append(i)

    #   Counting each option
    for i in list_of_options:
        count_of_options.append(list_.count(i))

    #   Selecting the bigger
    bigger_index = 0
    for n, i in enumerate(count_of_options):
        if i > bigger_index:
            bigger_index = n
    
    return list_[bigger_index]


#   Solution 2 (dicts usually makes things easier)
def majority_vote(list_):
    options_dict = {key: list_.count(key) for key in list_}

    equal = list(options_dict.values())[0]
    #  Check for equality

    
    for key, value in options_dict.items():
        if value == max(options_dict.values()):
            return key
    return options_dict



print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))