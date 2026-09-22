from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window: represents char in our window rn
        # variation: k represents lives we have to swap chars with
        # we decrement it when the char is != maxFreqChar.
        # trigger: if window size(5) - max freq char(3) > k:
        # we will then need to shift ptr left, and remove -= 1 of the key from hashmap.
        # at each window grow, we will want to shift right and log that size into max.
        # return max.

        window = defaultdict(int)
        l = 0
        best = 0
        
        for r in range(len(s)):
            # 1. grow the window
            window[s[r]] += 1

            # 2. validate and shrink until window is valid (maxReplacements <= k)
            maxFreq = max(window.values()) # gets highest freq char count
            windowSize = r - l + 1
            maxReplaces = windowSize - maxFreq

            while maxReplaces > k:
                window[s[l]] -= 1
                l += 1

                maxFreq = max(window.values()) # gets highest freq char count
                windowSize = r - l + 1
                maxReplaces = windowSize - maxFreq

            # 3. now it is safe, store the valid window
            best = max(best, windowSize)
            
        return best