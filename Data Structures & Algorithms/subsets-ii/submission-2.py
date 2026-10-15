class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # allows us to skip duplicates.
        path = []
        res = []

        # dfs need no params, will be using the global path and res
        def dfs(i):
            # base cases.
            # path max size.
            if i == len(nums):
                res.append(path.copy())
                return
            
            # path might not be max len... but we go over every iter right?
            # we can ensure this in a loop...

            # at every iter what do we do?, decide if we keep or scrap number.
            path.append(nums[i])
            nextIter = i + 1

            # this will try 1 route first not removing the duplicates right away for the og path.

            # 1. choose current branch
            dfs(nextIter)

            # 2. remove current choice
            path.pop()

            # 3. remove all duplicate, find next value.
            # must not go over duplicate values, since it will generate the same answer. This will trigger once the og path finishing solving the original long path.

            while nextIter < len(nums) and nums[nextIter] == nums[i]:
                # print(f"hit: {nextIter}, next val: {nums[nextIter]}, curr val: {nums[i]}")
                nextIter += 1
            



            # 4. explore path at next unique value, guranteed by while loop at 3.
            dfs(nextIter)
            
        # call from source
        dfs(0)
        return res

        # [1,1,2]
        # []
        # [1]
        # [1,1]