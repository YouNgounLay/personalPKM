import string

class Node: 
    def __init__(self): 
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self): 
        self.root = Node()

    def insert(self, word): 
        word = word.lower()
        cursor = self.root
        for letter in word: 
            if cursor.children[ord(letter) - ord('a')] == None:
                cursor.children[ord(letter) - ord('a')] = Node()
            cursor = cursor.children[ord(letter) - ord('a')]
        cursor.isEndOfWord = True
        return self

    def search(self, key):
        return self.isMatch(key, self.root, 0, True)
    
    def startWith(self, prefix):
        return self.isMatch(prefix, self.root, 0, False)
        
    
    def isMatch(self, word, node, index, isFullMatch):
        if node == None:
            return False

        if index == len(word):
            return not isFullMatch or node.isEndOfWord
        
        return self.isMatch(word, node.children[ord(word[index]) - ord('a')], index+1, isFullMatch)
        ...


if __name__ == "__main__": 
    trie = Trie()
    trie.insert("cat").insert("discombobulate")
    trie.insert("catan").insert("disconnect")
    print(trie.search("cat"))
    print(trie.search("dog"))
    print(trie.startWith("ca"))
    print(trie.startWith("dis"))
