'''
Parentheses Clusters
Write a function that groups a string into parentheses clusters. Each cluster 
should be balanced.

Examples
split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
Notes
All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) 
in the same cluster.
'''

def split(parenthesis):
    opened_count = 0
    temp = ''
    result = []
    for par in parenthesis:
        if par == '(':
            opened_count += 1
            temp += par
        elif par == ')':
            opened_count -= 1
            temp += par
        
        if opened_count == 0:
            result.append(temp)
            temp = ''

    return result

if __name__ == '__main__':
    print(
        split("()()()"),
        split("((()))"),
        split("((()))(())()()(()())"),
        split("((())())(()(()()))")
    )
    