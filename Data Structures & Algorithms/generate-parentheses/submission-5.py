class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # given n, return all valid n permutations

        res = []
        path = []

        # at every iteration, we either close the bracket, or leave open, up n max open.
        # len(path) is capped at 2 * n, which means we close our path then.
        # this could be our base case.


        # we will be comparing the len of path or i, to 2*n
        def dfs(opened, closed):
            if (opened == n and closed == n):
                res.append("".join(path.copy()))
                return

            # how do we maintain the state of how many open or close we have?
            # what do we need to know?
            # 1. how many open brackets we have
            # 2. at every iter: if < maxOpenBracket, do we want to "(" or ")"
            # 3. must be a valid closing.. so check the last element of path?
            # 4. maybe we need to maintain openBrackets, closeBrackets?

            # closed must always be less than opened until last one.
            if opened < n:
                path.append("(")
                # this now explores all path starting with this ( append
                dfs(opened + 1, closed)
                path.pop()

            if closed < opened:
                path.append(")")
                # this now explores all path starting with this ) append
                dfs(opened, closed + 1)
                path.pop()

        dfs(0,0)
        return res
            
