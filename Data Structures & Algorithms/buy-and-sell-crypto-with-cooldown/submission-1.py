class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, canBuy):
            if len(prices) <= i:
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            if canBuy:
                buy = dfs(i + 1, not canBuy) - prices[i]
                cooldown = dfs(i + 1, canBuy)
                dp[(i, canBuy)] = max(buy, cooldown) 
            else:
                sell = dfs(i + 2, not canBuy) + prices[i]
                cooldown = dfs(i + 1, canBuy)
                dp[(i, canBuy)] = max(sell, cooldown)
            return dp[(i, canBuy)]
        
        return dfs(0, True)