# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

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
prices = [7, 1, 5, 3, 6, 4]

s = Solution()
print(s.maxProfit(prices))