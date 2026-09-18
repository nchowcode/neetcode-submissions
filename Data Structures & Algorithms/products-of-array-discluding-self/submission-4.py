class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # essentially prefix and postfix.
        # must be double pass lists
        # [0,1,2,3] indexes
        # [1,2,4,6] input

        # [1,2,8,48] L-> R
        # [48,48,24,6] R->L

        # [48,24,12,8]
        # lets try brute force

        # pattern is for each i, look at i-1 on prefix, i+i on postfix, if out of bounds, assume * 1.

        prefix = []
        postfix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                new_num = nums[i] * prefix[-1]
                prefix.append(new_num)
        
        for i in range(len(nums) -1 ,-1,-1):
            if i == len(nums)-1:
                postfix.append(nums[i])
            else:
                postfix.append(nums[i] * postfix[-1])
        postfix.reverse()

        res = []
        for i in range(len(nums)):
            start = 0
            end = len(nums) - 1
            if i == start:
                res.append(postfix[i + 1])
            elif i == end:
                res.append(prefix[i - 1])
            else:
                total = prefix[i - 1] * postfix[i + 1]
                res.append(total)
        return res
