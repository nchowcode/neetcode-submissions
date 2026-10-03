import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)
        print
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        stack = []

        for _ in range(self.k):
            # print("1")
            poppedVal = heapq.heappop(self.heap)
            # heap rebalanced...
            # 
            stack.append(-poppedVal)

        value = stack[-1]
        for p in stack:
            heapq.heappush(self.heap, -p)

        return value
        
