class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            curr_profit = max(0, curr_profit+diff)
            max_profit = max(max_profit, curr_profit)

    
        return max_profit


'''
max_profit = 0
curr_profit = 0
loop through the lenth of prices
    diff = prices[i+1] - prices[i]
    curr_profit = max(0, diff+curr_profit)
    max_profit = max(max_profit, curr_profit)
    
return max_profit


TC: O(N), we loop through the prices array once
SC: O(1), no extra data structures, just a few variables
'''