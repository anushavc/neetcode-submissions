class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Stage 1: Fill with "impossible"
        fewest = [amount + 1] * (amount + 1)

        # Stage 2: Easy spot
        fewest[0] = 0

        # Stage 3: Every amount, try every coin
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    fewest[a] = min(fewest[a], 1 + fewest[a - c])

        # Stage 4: Still impossible? → -1
        if fewest[amount] == amount + 1:
            return -1
        return fewest[amount]