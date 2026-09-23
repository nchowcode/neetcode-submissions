class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # notice we have <=, rather than <? cus we are finding exact target.
        while l <= r:
            middle = (l + r) // 2
            
            if target == nums[middle]:
                return middle
            

            if nums[l] <= nums[middle]: #means its sorted.
                # is the target in here? the sorted half?
                if nums[l] <= target <= nums[middle]:
                    r = middle
                else:
                    l = middle + 1
            # otherwise other half is sorted.
            else:
                if nums[middle] <= target <= nums[r]: 
                    l = middle + 1
                else:
                    r = middle - 1

        # it has to be in the while loop, otherwise it doesnt exist.
        return -1