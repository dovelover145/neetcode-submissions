class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        dp = [[1] * COLS for _ in range(ROWS)]

        for i in range(ROWS - 2, -1, -1):
            for j in range(COLS - 2, -1, -1):
                
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
                