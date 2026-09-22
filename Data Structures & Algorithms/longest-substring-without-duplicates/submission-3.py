class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = 0
        best = 0

        for r in range(len(s)):
            char = s[r]

            # If this character is already inside the current window,
            # jump l beyond its previous occurrence.
            if char in window and window[char] >= l:
                l = window[char] + 1

            # Store the character's most recent index.
            window[char] = r

            length = r - l + 1
            best = max(best, length)

        return best