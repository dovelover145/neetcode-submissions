class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        max_area = 0
        cur_area = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(i, j):
            nonlocal cur_area
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                cur_area += 1
                grid[i][j] = 0
                for i_d, j_d in directions:
                    dfs(i + i_d, j + j_d)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    max_area = max(max_area, cur_area)
                    cur_area = 0
        
        return max_area
