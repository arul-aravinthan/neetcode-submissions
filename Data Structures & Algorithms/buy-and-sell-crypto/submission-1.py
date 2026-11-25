class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        #prices - [1,5,9,27,2,5]
        # [3,5,2,19,20,5]
        max_profit = 0
        for r in range(len(prices)):
            max_profit = max(max_profit, prices[r] - prices[l])
            #if the price we're at now is lower than our old buying price, it won't hurt to move to 
            #here for future windows. 
            if prices[r] < prices[l]:
                l = r
        return max_profit