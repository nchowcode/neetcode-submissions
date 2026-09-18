from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # uniqueness in: row, col, sub boxes.

        colMap = defaultdict(set) # col1:set()...
        rowMap = defaultdict(set)
        boxMap = defaultdict(set)
        # [0,0 -> 2,2], [3,0 -> 5,2]
        size = 9

        for c in range(size):
            for r in range(size):
                val = board[r][c]

                if val == ".":
                    continue
                box = (r // 3, c // 3)
                if val in colMap[c] or val in rowMap[r] or val in boxMap[box]:
                    return False
                else:
                    colMap[c].add(val)
                    rowMap[r].add(val)
                    boxMap[box].add(val)

        return True