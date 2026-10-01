class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                newNode = TrieNode()
                node.children[char] = newNode
            
            node = node.children[char]
        
        # mark end marker
        node.isWord = True

    def search(self, word: str) -> bool:
        # start from root
        # go until you find isWord.
        # fail early as soon as not present

        node = self.root
        for char in word:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        
        return True