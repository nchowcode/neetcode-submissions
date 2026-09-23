from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # find shortest substring of "S" that contains "T"
        # we need to start big -> collapse.
        # have a running min that calculates size and the the indices that contain the str "L:R"

        # question: is it pinch method? is it slow fast method? sliding window from left.
        # it is the only one to get full coverage with the right ptr.


        l = 0
        currWindow = defaultdict(int)
        need = defaultdict(int)
         # represents each char boolean check. 
        have = 0
        # pre-processing
        for c in t:
            need[c] += 1
        
        best = float("inf")
        bestStr = (0,0)

        required = len(need)

        for r in range(len(s)):
            char = s[r]
            currWindow[char] += 1

            if char in need and currWindow[char] == need[char]:
                have += 1

            # if we have enough... trim
            while have == required:
                windowLength = r - l + 1

                if windowLength < best:
                    best = windowLength
                    bestStr = (l,r)

                removed = s[l]
                currWindow[removed] -= 1

                if removed in need and currWindow[removed] < need[removed]:
                    have -= 1
                l += 1

            # at this point, it is alr as lean as possible capturing min valid length.

        if best == float("inf"):
            return ""
            
        return s[bestStr[0]:bestStr[1]+1]
        
