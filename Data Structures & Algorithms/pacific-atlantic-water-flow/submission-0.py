class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visited, atlantic_visited = set(), set()

        def dfs(r, c, visited, prev_height):
            if 0 <= r < ROWS and 0 <= c < COLS and not ((r, c) in visited) and prev_height <= heights[r][c]:
                visited.add((r, c))
                dfs(r - 1, c, visited, heights[r][c])
                dfs(r + 1, c, visited, heights[r][c])
                dfs(r, c - 1, visited, heights[r][c])
                dfs(r, c + 1, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific_visited, heights[r][0])
            dfs(r, COLS - 1, atlantic_visited, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pacific_visited, heights[0][c])
            dfs(ROWS - 1, c, atlantic_visited, heights[ROWS - 1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    res.append((r, c))
        
        return res
        