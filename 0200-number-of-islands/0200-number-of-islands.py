class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i,j):
            if grid[i][j] == "1":

                grid[i][j] = "L"
          
                if i > 0:              dfs(i-1,j)  # move up
                if i < len(grid)-1:    dfs(i+1,j)  # move down
                if j > 0:              dfs(i,j-1)   # move left
                if j < len(grid[0])-1: dfs(i,j+1)  # move right

            else:
                return

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands +=1
                    dfs(r,c)
        
        return islands
            
        