class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # o(n) constraint = no sorting
        # essentially checking for sequential numbers from input.

        # maybe transform it into a set. allows for constant time lookup.
        # logic:
        # for any num, it is either start or extension.
        # start = no nums prior
        # extend = nums prior
        numsSet = set(nums)
        longest = 0
        for n in nums:
            currLen = 1
            if n - 1 in numsSet:
                continue
            else:
                while n + 1 in numsSet:
                    currLen += 1
                    n += 1
                longest = max(longest, currLen)
        return longest