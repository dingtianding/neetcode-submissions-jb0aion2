class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(x, y):
            if (x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] == "0"):
                return #stop if out of range or not island
            grid[x][y] = "0"
            for dx, dy in directions:
                dfs(x + dx, y+ dy)

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == "1":#found an island
                    dfs(x, y) #explore rest of the island
                    res += 1
        return res
        