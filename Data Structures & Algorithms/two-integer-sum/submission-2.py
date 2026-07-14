from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # preload hashmap with num + indice
        # key = target - curr.
        # if diff in hashmap, then return indice

        # {5 : 1}
        targetMap = defaultdict(int)


        for index, value in enumerate(nums):
            if value in targetMap:
                return [targetMap[value], index]
            else:
                diff = target - value
                targetMap[diff] = index

        return [0,0]