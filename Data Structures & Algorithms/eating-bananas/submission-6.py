import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # running binary search on possible answers.
        # we know that the max(piles) will gurantee valid answer, a 1 stack/hour for sure
        # we need to find the minimum possible answer.
        # if hours == h: we have secured it... or it indicates that it is closer.
        # now... 
        
        l = 1
        r = max(piles)

        while l < r:
            middle = (l + r) // 2
            hours = 0
            
            # calculate total hours given a speed.
            for pile in piles:
                time = math.ceil(pile / middle)
                hours += time

            # finished in 8 : need to be done in 4
            # we want the lowest speed, aka lowest while being at most h.

            # too slow...
            if hours > h:
                l = middle + 1
            elif hours <= h:
                r = middle
        
        return l


