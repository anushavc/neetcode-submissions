class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Optimized
        #we are trying to buy lowest and sell highest for max Profit
        min_price=prices[0]
        maximum_profit=0
        #suppose while traversing we see an element higher than the min price, then we will compute the max profit. if it is lower than min price, we will update the min price
        for i in range(0,len(prices)):
            min_price=min(min_price,prices[i])
            maximum_profit=max(maximum_profit,prices[i]-min_price)
        return maximum_profit
        
