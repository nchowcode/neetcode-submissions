class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set is ideal.
        # brute force would be ok i have 1, let me check down entire list to see if i have 1, not store any state
        # ideal: use a set, store curr num, check against set, if not in, add, if we sweep through all, and is safe then pass.

        check = set()

        for num in nums:
            if num in check:
                return True
            else:
                check.add(num)
        return False