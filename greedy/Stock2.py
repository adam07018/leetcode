# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        sell = 0
        for sell in prices:
            if sell > buy:
                profit += sell - buy
            buy = sell
        return profit
    
prices = [7,1,5,3,6,4]
print(Solution.maxProfit(Solution,prices))
