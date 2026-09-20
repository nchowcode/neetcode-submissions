class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4,-1,-1,0,1,2]

        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            prev = i - 1
            if i > 0 and nums[i] == nums[prev]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append([nums[i],nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
            