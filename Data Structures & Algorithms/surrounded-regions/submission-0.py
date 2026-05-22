class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def capture(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                board[r][c] = "T"
                for rd, cd in DIRECTIONS:
                    capture(r + rd, c + cd)

        # Capture unsurrounded regions
        for r in range(ROWS):
            capture(r, 0)
            capture(r, COLS - 1)
        
        for c in range(COLS):
            capture(0, c)
            capture(ROWS - 1, c)

        # Capture surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
        # Uncapture unsurrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
