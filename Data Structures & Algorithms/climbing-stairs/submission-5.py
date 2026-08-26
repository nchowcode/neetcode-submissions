class Solution:
    def climbStairs(self, n: int) -> int:
        # Practice top-down first, because it teaches you how to derive the solution:
        # Start with the full problem: ways(n).
        # Ask what choices are possible.
            # 1 step or 2 step
        # Turn those choices into smaller problems.
            # 1 step -> n - 1, 2 step -> n - 2
        # Identify when the problem becomes trivial.
            # trivial when n is 2 or 1, so we just + 1
        # Add memoization when states repeat.

        dp = [0] * (n + 1)

        def ways(n):
            if n <= 2:
                return n
            
            if dp[n] != 0:
                return dp[n]

            dp[n] = ways(n - 1) + ways(n-2)

            return dp[n]


        # store current one into dp
        
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        

        return ways(n)