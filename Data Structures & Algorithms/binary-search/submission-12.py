class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                r = middle - 1

            else:
                l = middle + 1
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r

        return -1