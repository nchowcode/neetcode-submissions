class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # pre-processing to build Trie

        # Questions:
        # how will i know if a sequence of chars in our board is a word?
        # even if i try to pre-process, it will be difficult to identify and mark words
        # words is what im looking for, we reference the board/another datastructure to validate it
        # word ladder = trie
        # repeated work is trying out m*n options give a singular word
        # there are multiple chars in board as well, making it hard to identify.


        # Clarifications
        # 1. build trie
        # 2. search the trie for the words
        # 3. output

        # 1. build trie
        root = TrieNode()
        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]
            
            # mark end of word + have word accessible
            node.word = word
        # trie is now fully built

        # 2. search through the board now.
        # note: why trie is good? it lets us exit early as we have constant access to words, rather than n*m*chars
        res = []

        def dfs(row,col,node) -> bool:
            directions = [(row, col + 1),(row, col - 1), (row + 1, col), (row - 1, col)]
            nonlocal res
            # boundaries
            if col < 0 or col > len(board[0]) - 1 or row < 0 or row > len(board) - 1:
                return

            if board[row][col] == "#":
                return

            char = board[row][col]
            if char not in node.children:
                return

            # if word, happy case, but.... we also need to account for "cat, cats" cant end early
            nextNode = node.children[char]                
            
            # check word and add into final list
            if nextNode.word:
                res.append(nextNode.word)

                nextNode.word = None # mark as visited to not allow "cat" and "cats"
            
            # mark visited
            board[row][col] = "#"

            # keep traversing recursively
            for r,c in directions:
                dfs(r,c,nextNode)

            # once done traversing, we can mark it for other paths
            board[row][col] = char
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root)

        return res
            

            



