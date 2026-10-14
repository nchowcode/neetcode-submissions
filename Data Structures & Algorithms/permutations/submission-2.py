class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        def dfs():
            # base case
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in used:
                    continue

                # 1. choose num
                path.append(num)
                used.add(num)

                # 2. explore options
                dfs()

                # 3. undo
                last = path.pop()
                used.remove(last)

        
        dfs()
        return res
            



