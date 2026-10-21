class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # area is basically where traversal covers, except instead of no-op, we increment the parent call by 1.
        # we would want to store the max of these, so we'd just take the max at the bottom of the dfs call that was returned by it.

        # static vars
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        land = 1
        water = 0

        # dfs func
        def dfs(row, col) -> int:
            # out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            
            # no op
            if grid[row][col] == water:
                return 0
            
            # mark as visited...
            grid[row][col] = water

            # otherwise we return the total...
            up = dfs(row - 1, col)
            down = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)

            return 1 + (up + down + left + right)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == land:
                    size = dfs(row,col)
                    maxArea = max(maxArea, size)

        return maxArea