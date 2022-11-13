def solution(sequence):
    my_dict = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    inverse_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    oppened_cursors = [] 

    for char in sequence:
        # When opening check
        if char in my_dict.keys():
            oppened_cursors.append(char)

        # When closing check
        if char in inverse_dict.keys():
            # Check if closing bracket is oppened
            if inverse_dict[char] in oppened_cursors:
                # Check if it is closing the right bracket
                if inverse_dict[char] != oppened_cursors[-1]:
                    return False
                else:
                    oppened_cursors.remove(inverse_dict[char])

            else:
                return False
    
    # Check if we have not closed chars
    return True if not oppened_cursors else False


print(solution('{[]}'))
print(solution('{{[]}}'))
print(solution('{[}'))
print(solution('[{]}'))