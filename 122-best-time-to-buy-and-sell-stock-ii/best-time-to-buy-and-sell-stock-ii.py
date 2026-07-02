class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for r in range(l, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = profit + prices[r] - prices[l]
                l = r
        return profit