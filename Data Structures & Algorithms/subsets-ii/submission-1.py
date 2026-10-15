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
            print(path.copy())
            nextIter = i + 1

            # this will try 1 route first not removing the duplicates right away for the og path.

            dfs(nextIter)
            # must not go over duplicate values, since it will generate the same answer. This will trigger once the og path finishing solving the original long path.

            while nextIter < len(nums) and nums[nextIter] == nums[i]:
                # print(f"hit: {nextIter}, next val: {nums[nextIter]}, curr val: {nums[i]}")
                nextIter += 1
            

            # 2. ignore current value.
            path.pop()

            # try to explore path again, ignoring the duplicate start point, pushed to the next val.
            dfs(nextIter)
            

        dfs(0)
        return res

        # [1,1,2]
        # []
        # [1]
        # [1,1]