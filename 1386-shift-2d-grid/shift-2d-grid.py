class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        # n = len(grid)
        # m = len(grid[0])
        # size = m*n 
        # k %= size 
        # if k == 0:
        #     return grid

        # grid_1D = [ grid[i][j] for i in range(n) for j in range(m) ]
        # grid_1D += grid_1D 
        
        # indx = size-k
        # for i in range(n):
        #     for j in range(m):
        #         grid[i][j] = grid_1D[indx]
        #         indx +=1

        # return grid 

#------------------------------------------------------------------------

        m = len(grid)
        n = len(grid[0])
        k %= m*n
        if k == 0:
            return grid

        grid_1D = [ grid[i][j] for i in range(m) for j in range(n) ]
        grid_1D = grid_1D[-k:]+grid_1D[:-k]

        return [ grid_1D[i*n:i*n+n] for i in range(m) ]








        