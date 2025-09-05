import string

class Node: 
    def __init__(self, value="a"): 
        self.value = value
        self.children = list(string.ascii_lowercase)

class Trie:
    def __init__(self, root):
        self.root = root
