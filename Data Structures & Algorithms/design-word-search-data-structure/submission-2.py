class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                newTrieNode = TrieNode()
                node.children[char] = newTrieNode
            node = node.children[char]
        node.isWord = True
    def search(self, word: str) -> bool:
        # only difference is account for .

        def dfs(index, node) -> bool or str:
            if index == len(word):
                return node.isWord

            char = word[index]
            # 1. wildcard = traverse all children to see if any return true.
            if char == ".":
                for child in node.children: # child = "a" "b"
                    childNode = node.children[child]
                    res = dfs(index + 1, childNode)
                    if res: return True
                return False

            # 2. normal char
            if char in node.children:
                return dfs(index + 1, node.children[char])
            
            # 3. char doesnt exist... all else
            return False

        root = self.root

        return dfs(0, root)