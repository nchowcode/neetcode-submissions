from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram is the same word, scrambled anyways
        # how do we check if its the same word? its gonna be by char count. If we sort them, they will also be the same.
        # 2 approaches: [o(n) space, o(n)] time vs [nlogn time, o(1) space]
        hashmapS = defaultdict(int)
        hashmapT = defaultdict(int)
        # hash s
        lenS = len(s)
        lenT = len(t)

        if lenS != lenT:
            return False
        
        for i in range(lenS):
            hashmapS[s[i]] += 1
            hashmapT[t[i]] += 1

        return hashmapS == hashmapT

        