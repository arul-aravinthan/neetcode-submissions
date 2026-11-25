class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices - [1,5,9,27,2,5]
        # init two pointers, move pointer that would improve it most at each step. 
        # would this remove good solutions if we tried it?
        # [3,5,2,19,20,5]
        buy = prices[0]
        profit = 0
        for price_idx in range(len(prices)):
            #curr price - buy price 
            profit = max(profit, prices[price_idx] - buy)
            #take the min of whatever we've seen, and that is our new buy price in the future
            #intuition is that for future selling points, we only care about what the cheapest thing 
            #we've seen is
            buy = min(prices[price_idx], buy)
        return profit 