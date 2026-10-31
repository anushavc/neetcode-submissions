class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        l,r=0,1
        while r<len(prices):
            #if todays price is greater than buy price, we record profit and move sell pointer to right (r)
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                max_profit=max(max_profit,profit)
            else:
                l=r
            r=r+1
        return max_profit

