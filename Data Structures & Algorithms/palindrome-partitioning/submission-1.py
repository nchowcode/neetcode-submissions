class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # base case = any solo word.
        # backtracking on index in s
        # we need a path string builder copy
        # a helper palindrome function.




        path = []
        res = []
        end = len(s)
        def dfs(start):
            # base case
            if start == len(s):
                res.append(path.copy())
                return
            
            # if current piece is palindrome, we add to path
            # 1. [start:i] is valid -> append it to path.
            # 2. dfs(i)
            # the challenge is... what do we pass into the palindrome?
            # then we send in end piece to recursive.

            # [valid: rest]
            for end in range(start, len(s)):
                # we want to check if its a valid palindrome from start:end + 1
                if isPalindrome(start, end):
                    path.append(s[start:end +1])
                    dfs(end + 1)
                    path.pop()
                # if its not a palindrome, we keep pushing the boundary.

        def isPalindrome(l,r) -> bool:
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        dfs(0)
        return res
                