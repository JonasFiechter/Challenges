'''
Super Reduced String
Steve has a string of lowercase characters in range ascii[["a".."z"]]. He wants 
to reduce the string to its shortest length by doing a series of operations. In 
each operation, he selects a pair of adjacent lowercase letters that match, and 
he deletes them. For instance, the string aab could be shortened to b in one 
operation.

Steve’s task is to delete as many characters as possible using this method and 
print the resulting string. If the final string is empty, return "Empty String".

Case
reduced_string("aaabccddd") ➞ "abd"
Explanation:

"aaabccddd" -> "abccddd" -> "abddd" -> "abd"
Examples
reduced_string("cccxllyyy") ➞ "cxy"

reduced_string("aa") ➞ "Empty String"

reduced_string("baab") ➞ "Empty String"

reduced_string("fghiiijkllmnnno") ➞ "fghijkmno"

reduced_string("chklssstt") ➞ "chkls"
'''

def reduced_string(string):
    def delete_adjacent(index_list, string):
        new_string = ''
        for index, item in enumerate(string):
            if index not in index_list:
                new_string += item
                
        return new_string
    
    def check_adjacent(string):
        for index in range(len(string) -1):
            if string[index] == string[index +1]:
                return True
        return False
    
    def find_adjacent(string):
        for index in range(len(string) -1):
            if string[index] == string[index +1]:
                return [index, index +1]
        return False
    
    while check_adjacent(string):
        string = delete_adjacent(find_adjacent(string), string)

    return string if string else 'Empty String'

if __name__ == '__main__':
    print(reduced_string("aaabccddd"))
    print(reduced_string("cccxllyyy"))
    print(reduced_string("aa"))
    print(reduced_string("baab"))
    print(reduced_string("fghiiijkllmnnno"))
    print(reduced_string("chklssstt"))
    print(reduced_string(""))
    print(reduced_string("acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj"))