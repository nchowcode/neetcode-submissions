class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # path step: to exclude or include curr number
        # we are building subset, only appending when valid,

        res = []
        subset = []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return

            if i == len(nums) or remaining < 0: # prune
                return

            subset.append(nums[i])

            dfs(i, remaining - nums[i])

            subset.pop()

            dfs(i + 1, remaining)


        dfs(0, target)
        return res
            


            


            