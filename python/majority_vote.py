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

#  Solution 1
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
    
    print(count_of_options)



majority_vote(["A", "A", "A", "B", "C", "A"])