import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # so we are basically shrinking the stones to 1.
        # base case = 1 or 0, idk when 0...
        # 2->1, 1 no op

        # 1. heapify stones
        # 2. check len of stones, if len > 1: op, else return stone
        # 3. repeat 2 until 1 remain.

        heapq.heapify_max(stones)

        # pre check:

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x == y:
                continue
            
            if x > y:
                x = x - y
                heapq.heappush_max(stones, x)
            
            elif y > x:
                y = y - x
                heapq.heappush_max(stones, y)
        
        return stones[0] if stones else 0
