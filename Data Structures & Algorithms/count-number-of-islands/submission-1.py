class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # pretty obv by patter this is a dfs problem.
        # dfs extends as far as the curr block is a 1, will stop on 0.
        # once that entire loop ends, we increment island by 1.
        # next iter, we find the next island start, dfs will traverse and clear all islands and flip them.
        
        # shape:

        # dfs...
        # for i
        #   for j
        #        dfs...

        # static vars
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        island = "1"
        water = "0"

        # dfs -> dfs on diff coords, so param is row, col
        def dfs(row, col):
            # out of bounds > landtype > action
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # base case
            if grid[row][col] == water:
                return
            
            # mark "visited", but still travel
            if grid[row][col] == island:
                grid[row][col] = "0"

            # action step / queue
            up = dfs(row - 1, col)
            down = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)

            # at this point all the flips complete, we can just return
            return

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == island:
                    dfs(row, col)
                    total += 1
        
        return total



