class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        fresh_oranges = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    rn, cn = r + dr, c + dc
                    if 0 <= rn < ROWS and 0 <= cn < COLS and grid[rn][cn] == 1:
                        grid[rn][cn] = 2
                        fresh_oranges -= 1
                        q.append((rn, cn))
            
            time += 1
        
        return -1 if fresh_oranges else time
