class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Optimized
        min_price=prices[0]
        max_profit=0
        for i in range(0,len(prices)):
            min_price=min(min_price,prices[i])
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit