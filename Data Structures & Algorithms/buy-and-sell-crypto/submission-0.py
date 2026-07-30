class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if minimum>prices[i]:
                minimum=prices[i]
            elif minimum<prices[i]:
                max_profit=max(max_profit,(prices[i]-minimum))
        return max_profit

        