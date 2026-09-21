class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        n = len(prices)
        r = n - 1

        for i in range(n):
            localMax = 0
            for j in range(i, n):
                localMax = prices[j] - prices[i]
                maxProfit = max(maxProfit, localMax)

        return maxProfit
            
