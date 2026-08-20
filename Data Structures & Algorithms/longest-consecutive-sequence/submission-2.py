class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        # we want to see if starting seq or not, meaning its used later
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
