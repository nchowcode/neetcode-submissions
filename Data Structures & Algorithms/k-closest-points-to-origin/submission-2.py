import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # very clearly a heap problem, where we must attach a score to it in comparison to the origin
        # 1. figure out how to heapify a list with specific guide lines / lambda
        # 1. transform each value into a tuple, (key (priority), original)

        # 2. for _ in range: pop val

        
        priorityKey = lambda x : math.sqrt((x[0])**2 + (x[1])**2)
        minHeap = [(priorityKey(x),x) for x in points]
        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res