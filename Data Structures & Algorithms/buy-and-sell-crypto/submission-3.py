class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        r = 1

        n = len(prices)

        if n < 2:
            return 0

        while r < n:
            profit = prices[r] - prices[l]
            best = max(best, profit)

            # swap buy date IF current date is lower
            if prices[r] < prices[l]:
                l = r
            r += 1

        return best

            
