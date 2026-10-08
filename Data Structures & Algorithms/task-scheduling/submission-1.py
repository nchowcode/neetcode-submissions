from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq measures how many are left, will be empty when val = 0.
        # heap, orders it by freq remaining, prioritizing it
        freq = Counter(tasks)

        # at every step, what choice do i need to make?
        # 1. decide which letter to consume
        # 2. is consume allowed?
        # 3. when is it possible to consume letter again?

        # maxHeap for prioritization. time check for allow, update time IF letter consumed, decrement letter after.


        # represents the copies in desc order
        heap = [freq for freq in freq.values()]
        heapq.heapify_max(heap)
        
        # we need a cooldown queue, (copiesRemaining, readyTime)
        cooldown = deque()
        time = 0

        while heap or cooldown:
            while cooldown and cooldown[0][1] <= time:
                copies, readyTime = cooldown.popleft()
                heapq.heappush_max(heap, copies)
            # pre-decremented copies count when pushing into queue...

            if heap: # rdy to be consumed
                copies = heapq.heappop_max(heap)
                copies -= 1
                if copies > 0:
                    cooldown.append((copies, time + n + 1))

            time += 1
        
        return time