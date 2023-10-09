# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

# Solution
class Solution:
    def maxProfit(self, prices):
        max_profit = 0

        # Compare adjacent elements, one-pass
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


# Driver
prices = [3,3,5,0,0,3,1,4]

s = Solution()
print(s.maxProfit(prices))