from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force would be check curr + rest = 7. for every n, check n-1 options to see if it matches.
        # optimized, store the diff and index, match it in a hashmap. at each iteration, we only need to know if target - curr exists at all, return index.

        hashmap = defaultdict(int)

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[val] = i
        return [0,0]