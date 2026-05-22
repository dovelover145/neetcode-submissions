class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited_pacific, visited_atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            if 0 <= r < ROWS and 0 <= c < COLS and not ((r, c) in visited) and prev_height <= heights[r][c]:
                visited.add((r, c))
                for dr, dc in DIRECTIONS:
                    dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, visited_pacific, heights[r][0])
            dfs(r, COLS - 1, visited_atlantic, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, visited_pacific, heights[0][c])
            dfs(ROWS - 1, c, visited_atlantic, heights[ROWS - 1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited_pacific and (r, c) in visited_atlantic:
                    res.append((r, c))
        
        return res
        