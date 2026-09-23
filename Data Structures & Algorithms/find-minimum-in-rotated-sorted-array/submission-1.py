class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # trick. we use binary search to not find a target, but to validate ordering.
        # we look at the middle, and compare it to the rightmost point.
        # we can then shrink the search pool.
        # final answer will be l == r.


        while l < r:
            middle = (l + r) // 2

            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle # since its <= ... meaning middle must be preserved.


        return nums[l]