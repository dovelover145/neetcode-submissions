class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                dp[i] = 0
                return 0
            
            if dp[i] >= 0:
                return dp[i]
            
            ways = 0
            ways += dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and "0" <= s[i + 1] <= "6")):
                ways += dfs(i + 2)
            
            dp[i] = ways
            return ways
        
        return dfs(0)