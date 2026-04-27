class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS,COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(x, y):
            if (x < 0 or y < 0 or x >= ROWS or y >= COLS):
                return
            if grid[x][y] == "0":
                return

            grid[x][y] = "0"
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == "1":
                    dfs(x,y)
                    res += 1
        return res
        