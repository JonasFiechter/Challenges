'''
Implement a Trie (Prefix Tree) and write a function to search for a word in the 
Trie.
'''

class TrieNode:
    def __init__(self):
        # Your code here
        ...

class Trie:
    def __init__(self):
        # Your code here
        ...
    
    def insert(self, word):
        # Your code here
        ...
    
    def search(self, word):
        # Your code here
        ...

# Test cases
if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # Output: True
    print(trie.search("app"))    # Output: False
    print(trie.search("appl"))   # Output: False