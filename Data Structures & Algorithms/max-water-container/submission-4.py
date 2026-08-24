class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_wall = 0
        right_wall = len(heights) - 1

        max_area = 0
        while left_wall < right_wall:
            # print(f"heights: {left_wall}:{heights[left_wall]}, {right_wall}:{heights[right_wall]}")
            # valid sequence.
            height = min(heights[left_wall], heights[right_wall])
            area = (right_wall - left_wall) * height

            max_area = max(area, max_area)

            if heights[right_wall] > heights[left_wall]:
                left_wall += 1
            else:
                right_wall -= 1

            
        return max_area
