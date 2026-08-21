class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Constraints: o(1) space
        # Key Notes: sorted -> perfect for Two Pointers
        # 2 pointer approach L and R, depending on > or <, increment L or R

        l = 0
        r = len(numbers) - 1

        while l < r:
            # calculate total -> too big = shift left ? too small = shift right
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1,r + 1]

    