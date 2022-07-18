'''
Find the Pattern
Given a dictionary containing up to six phrases, return a list containing the 
matching phrases according to the given string (p).
Ignore any digit that is placed after or before the given string.
Whether the first letter is capitalized or not, if all letters of the word match 
the given string (p), it is valid.
If it does not match the given string (p) then None.
Examples
find_pattern({
  "Phrase1": "COVID-19 is no good",
  "Phrase2": "COVID-18 is no good",
  "Phrase3": "COVID-17 is no good"
}, "COVID-19")

➞ ["Phrase1 = COVID-19", "Phrase2 = None", "Phrase3 = None"]
find_pattern({
  "Phrase1": "Edabit is great",
  "Phrase2": "Edabit is very great",
  "Phrase3": "Edabit is really great"
}, "really")

➞ ["Phrase1 = None", "Phrase2 = None", "Phrase3 = really"]
'''

# Solution 1
def find_pattern(phrase_dict, phrase):
    pattern_list = []
    for key, value in phrase_dict.items():
        if phrase.lower() in value.lower():
            pattern_list.append('' + key + ' = ' + phrase)
        else:
            pattern_list.append('' + key + ' = ' + 'None')

    return pattern_list

dict_for_test = {
  "Phrase1": "COVID-19 is no good",
  "Phrase2": "COVID-18 is no good",
  "Phrase3": "COVID-17 is no good"
}

print(find_pattern(dict_for_test, "COVID-19"))