class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} # (i, curAmount) = # of coin combinations for this path
        
        def dfs(i, curAmount):
            if curAmount < 0:
                return 0
            elif curAmount == 0:
                return 1
            else:
                combinations = 0
                for j in range(i, len(coins)):
                    if (j, curAmount) not in dp:
                        dp[(j, curAmount)] = dfs(j, curAmount - coins[j])
                    combinations += dp[(j, curAmount)]
                return combinations
        
        return dfs(0, amount)
