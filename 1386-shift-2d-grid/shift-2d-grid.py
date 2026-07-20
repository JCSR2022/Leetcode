class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n = len(grid)
        m = len(grid[0])
        size = m*n 
        k %= size 
        if k == 0:
            return grid


        grid_1D = [ grid[i][j] for i in range(n) for j in range(m) ]
        grid_1D += grid_1D 
        
        # print(n,m)
        # print(grid_1D)

        indx = size-k
        for i in range(n):
            for j in range(m):
                grid[i][j] = grid_1D[indx]
                indx +=1

        return grid 









        