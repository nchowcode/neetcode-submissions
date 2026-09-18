class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # very similiar to increasing temperature problem
        # this pattern:
        # calculate in monotonic increasing order.
        # the moment a shorter tower appears, pop all that are taller than curr shortest, then calc that area
        # we need to maintain its start index, since we can use the base of it to match the height of curr.
        
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
            else:
                # if stack, we must compare recent val to see if its taller
                start = i

                # prev tower is > curr height
                while stack and stack[-1][1] > h:
                    prevStart, prevHeight = stack.pop()
                    area = (i - prevStart) * prevHeight
                    maxArea = max(maxArea, area)
                    start = prevStart
                # however, we need to absorb most recently popped index
                
                stack.append((start,h))
        
        # if remaining values are in stack... calculate the rest... instead of curr i, we use len(heights)
        n = len(heights)
        while stack:
            prevStart, prevHeight = stack.pop()
            area = (n - prevStart) * prevHeight
            maxArea = max(maxArea, area)

        print(maxArea)
        return maxArea
