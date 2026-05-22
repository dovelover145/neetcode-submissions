class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        visited = set()
        
        def dfs(row, col, i):
            if i == len(word):
                return True
            if (0 <= row < ROWS) and (0 <= col < COLS) and ((row, col) not in visited) and (board[row][col] == word[i]):
                visited.add((row, col))
                res = dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1)
                visited.remove((row, col))
                return res
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False