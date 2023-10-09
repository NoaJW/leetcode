# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# My solution - Incorrect: when to pop min/max values such that min < max. Do one-pass method below, focus on buy/min price then go forwards for sell/max price
class MySolution:
    def maxProfit(self, prices):
        def getMaxPrice(prices): 
            min_value = min(prices)
            max_value = max(prices)
        
            # 0 max profit if min price == max price
            if min_value == max_value: 
                return 0

            # Put in lists the indexes for multiple occurences of min and max prices 
            min_idx = [idx for idx, val in enumerate(prices) if val == min_value]
            max_idx = [idx for idx, val in enumerate(prices) if val == max_value]

            # Day of min price has to be less than day of max price (buy before sell) to return a max profit, else 0
            if min(min_idx) < max(max_idx):
                return max_value - min_value
            else: 
                return max_idx   # Have caller go to second max value  
                
        sol = getMaxPrice(prices)

        while type(sol) is list:
            for i in sol: 
                prices.pop(i)       # remove max value(s). Remove until min value == max value or max profit is returned 
            sol = getMaxPrice(prices)
            
        return sol


# Solution
class Solution:
    def maxProfit(self, prices):
        # Initialize the minimum price to the first price and the max profit to 0
        min_price = prices[0]
        max_profit = 0

        # Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            # Update the minimum price if a lower price is found
            min_price = min(min_price, prices[i])
            # Update the max profit if a higher profit can be obtained
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit


# Driver
prices = [2, 4, 1]

s = Solution()
print(s.maxProfit(prices))
