class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        curRow = [1] * COLS

        for i in range(ROWS - 1):
            newRow = [1] * COLS
            for j in range(COLS - 2, -1, -1):
                newRow[j] = curRow[j] + newRow[j + 1]
            curRow = newRow
        
        return curRow[0]
