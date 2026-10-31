class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #logic: we want to buy when it is the lowest and we want to sell which it is the highest
        #condition: we have to buy first before we sell
        #reframe: two pointer approach #pointer: buy, pointer:sell
        max_profit=0
        l,r=0,1
        while r<len(prices):
            #logic: if the right pointer is greater to left pointer
            if prices[r]>prices[l]:
                max_profit=max(max_profit,prices[r]-prices[l])
            else:
                l=r
            r=r+1
        return max_profit


