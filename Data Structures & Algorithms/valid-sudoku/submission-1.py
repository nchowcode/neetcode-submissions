from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for c in range(9):
            for r in range(9):
                piece = board[c][r]
                if piece == ".":
                    continue
                
                # is it in any of the following:
                if piece in rows[r] or piece in cols[c] or piece in squares[(r//3,c//3)]:
                    return False
                else:
                    rows[r].add(piece)
                    cols[c].add(piece)
                    squares[(r//3,c//3)].add(piece)
        return True


                    
