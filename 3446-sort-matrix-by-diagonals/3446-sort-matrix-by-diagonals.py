class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        #brute force using sort function nLog(n) time

        n = len(grid)

        #bottom-left triangle 
        for i in range(n-1,-1,-1):
            curr_diag = []
            for j in range(0,n-i):
                curr_diag.append( grid[i+j][j] )
            curr_diag.sort(reverse =True)
            for j in range(0,n-i):
                grid[i+j][j] = curr_diag[j]

        #top-right triangle
        for j in range(1,n):
            curr_diag = []
            for i in range(n-j):
                curr_diag.append(grid[i][j+i])
                
            curr_diag.sort() 
            for i in range(n-j):
                grid[i][j+i] = curr_diag[i]

        return grid
            



        