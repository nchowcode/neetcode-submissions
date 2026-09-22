class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window with set representing window.
        # true if s2 contains s1 (size relevant)
        # trigger: window of size s1 on s2, create window set.
        # return true early, else shift r and left, on next iter, computate eqaulity

        s2window = defaultdict(int) # holds char in window
        s1window = defaultdict(int)
        n = len(s1)
        m = len(s2)
        l = 0
        for char in s1:
            s1window[char] += 1

        for char in s2[:n]:
            s2window[char] += 1

        if s1window == s2window:
            return True

        for r in range(n, m):

            s2window[s2[r]] += 1

            s2window[s2[l]] -= 1
            if s2window[s2[l]] == 0:
                del s2window[s2[l]]
            l += 1

            if s1window == s2window:
                return True
        
        return False

