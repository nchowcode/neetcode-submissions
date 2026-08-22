class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Rule: must be sorted to use 2 pointer
        # Key: perform 2 pointer by including current var

        # o(n^2)
        
        # pre-processing
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            curr = i
            curr_val = nums[curr]

            # exit early
            l = i + 1
            r = len(nums) - 1
            if curr_val > 0:
                break

            if i > 0 and curr_val == nums[i - 1]:
                continue

            while l < r:
                threesum = curr_val + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([curr_val, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicate starting value logic. 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                
            


            