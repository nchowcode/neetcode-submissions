from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given a list, and k, find the k most frequent numbers in list
        # aka, count the # of apperances of each num, sort it, and return the key.
        # tools: hashmap, num:occurences, return sorted() limit k

        hashmap = defaultdict(int)

        # ingestion
        for n in nums:
            hashmap[n] += 1
        
        # now hashmap has nums:occurence.

        # transformation
        topK = sorted(hashmap, key=hashmap.get, reverse=True)[:k]
        return topK
        

