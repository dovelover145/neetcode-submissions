class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue
                if dp[i - coin] == -1:
                    continue
                if dp[i] == -1 or (dp[i] > dp[i - coin] + 1):
                    dp[i] = dp[i - coin] + 1
        
        return dp[amount]
