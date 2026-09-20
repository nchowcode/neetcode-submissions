class Solution:
    def trap(self, height: List[int]) -> int:
        # use L and R approach
        l = 0
        r = len(height) - 1

        total = 0
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
        
        return total