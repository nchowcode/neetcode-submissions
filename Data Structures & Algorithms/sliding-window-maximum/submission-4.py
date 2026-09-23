import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            # if current window is built ->
            if i >= k - 1:

                # lazy deletion (only when size hits threshold and the index is stale and is root.)
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                
                # otherwise safe, append top that is valid.
                res.append(-heap[0][0])
        return res