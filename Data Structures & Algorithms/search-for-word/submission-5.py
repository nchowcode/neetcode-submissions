class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # boolean output if word can be constructed via board in valid moves.

        # rules: up, down, no reusing char for word, valid neighbors

        # 1. mark as visited.
        # 2. dfs(index, row, col)
        # 3. word[index] == list[row][col] and index == len(word)
        # 4. to backtrack... we need to undo the visited coordinates?... r
        # need to dfs all 4 directions and mark them as visited... we can't change the original state of the board tho... cus we need context to undo for other paths.

        # backtracking def involves the coordinates to resume to after no valid path is found.

        # 1. A no, B no, C yes! -> [B,A,D] -> does B match? no, does A match? yes!, does D match no!
        # 2. dfs(2, A coords..), [A, not c..., ] # we would need to mark the source as visited path.
        # dfs (3, T coords), if T matches AND 3 == len(targetWord).. return True.

        visited = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(index, row, col) -> bool:
            # out of bounds
            if (col < 0 or col >= cols) or (row < 0 or row >= rows):
                return

            # check if alr visited:
            if (row, col) in visited:
                return                
            
            # base case
            if index == len(word) - 1 and board[row][col] == word[index]:
                return True

            # bad case?
            if board[row][col] != word[index]:
                return False

            visited.add((row, col))
            # happy path case -> if word matches travel next
            left = dfs(index + 1, row, col - 1)
            right = dfs(index + 1, row, col + 1)
            up = dfs(index + 1, row - 1, col)
            down = dfs(index + 1, row + 1, col)

            # at this point we would have explored all options.
            visited.remove((row, col))

            return left or right or up or down


        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True
                else:
                    continue

        return False

