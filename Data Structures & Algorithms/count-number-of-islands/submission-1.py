class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        num_islands = 0

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                for i_d, j_d in directions:
                    dfs(i + i_d, j + j_d)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)

        return num_islands
