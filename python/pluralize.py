'''
Pluralize!
Given a list of words in the singular form, return a set of those words in the 
plural form if they appear more than once in the list.

Examples
pluralize() ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
Notes
This is an oversimplification of the English language so no edge cases will 
appear.
Only focus on whether or not to add an s to the ends of words.
All tests will be valid.
'''

#  Solution 1
def pluralize(list_):
    list_p = []
    for item in list_:
        if item in list_p or item + 's' in list_p:
            continue
        elif list_.count(item) == 1:
            list_p.append(item)
        else:
            list_p.append(item + 's')
    return list_p

#  Solution 2
def pluralize_2(list_):
    list_p = [word if list_.count(word) == 1 else word + 's' for word in list_]
    for index, item in enumerate(list_p):
        if list_p.count(item) > 1:
            list_p.pop(index)  
    return list_p

print(pluralize_2(["cow", "pig", "cow", "cow"]))
# print(pluralize(["table", "table", "table"]))
# print(pluralize(["chair", "pencil", "arm"]))