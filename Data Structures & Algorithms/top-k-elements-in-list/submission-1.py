from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # will be n log n to sort the values of the hashmap to desc
        tracker = defaultdict(int)

        for n in nums:
            tracker[n] += 1

        
        return (sorted(tracker, key = tracker.get, reverse=True)[:k])