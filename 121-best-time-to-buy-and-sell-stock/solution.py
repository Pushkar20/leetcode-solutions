class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1,p2 = 0,1
        profit = 0
        while p2 < len(prices) and p1 < len(prices):
            if (prices[p2] - prices[p1]) > profit:
                profit = prices[p2] - prices[p1]
                p2 += 1
            elif prices[p2] < prices[p1]:
                p1 = p2
                p2 = p1+1
            else:
                p2 += 1
        return profit
