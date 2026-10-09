class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int):
            # at each step, include or exclude
            if i == len(nums):
                res.append(subset.copy())
                return
             
            # 1. including: adding to subset
            subset.append(nums[i])
            # travel route
            dfs(i + 1)
            # exclude option
            subset.pop()
            # travel route
            dfs(i + 1)

        # triggers start
        dfs(0)

        # returns built after full traversal
        return res