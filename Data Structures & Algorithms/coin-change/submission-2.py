class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest=[amount+1]*(amount+1)
        fewest[0]=0
        for i in range(1,amount+1):
            for c in coins:
                #accounting for case where coin is too big
                if i>=c:
                    fewest[i]=min(fewest[i-c]+1,fewest[i])
        if fewest[-1]==(amount+1):
            return -1
        return fewest[-1]

