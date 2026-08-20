class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # goal: find the product of all nums excluding self
        
        # brute force: store the total product as single var and divide it by curr nums[i].

        # would not work for something with 0. ig if 0, make every other thing a 0. and ignore the operation?

        # without division... we can

        # [1, 2, 8, 48]
        # [48,48,24, 6]


        # prefix

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
