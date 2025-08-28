class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        #brute force using sort function nLog(n) time

        # n = len(grid)

        # #bottom-left triangle 
        # for i in range(n-1,-1,-1):
        #     curr_diag = []
        #     for j in range(0,n-i):
        #         curr_diag.append( grid[i+j][j] )
        #     curr_diag.sort(reverse =True)
        #     for j in range(0,n-i):
        #         grid[i+j][j] = curr_diag[j]

        # #top-right triangle
        # for j in range(1,n):
        #     curr_diag = []
        #     for i in range(n-j):
        #         curr_diag.append(grid[i][j+i])
                
        #     curr_diag.sort() 
        #     for i in range(n-j):
        #         grid[i][j+i] = curr_diag[i]

        # return grid
    #--------------------------------------------------------

    #same but i think a littel more comprehensive
        
        n = len(grid)
        #bottom-left triangle 
        for k in range(n):
            curr_diag = []
            j = 0
            for i in range(k,n):
                curr_diag.append(grid[i][j])
                j +=1
            curr_diag.sort(reverse=True)

            j = 0
            for i in range(k,n):
                grid[i][j] = curr_diag[j]
                j +=1


        # #top-right triangle
        for k in range(1,n):
            curr_diag = []
            i = 0
            for j in range(k,n):
                curr_diag.append(grid[i][j])
                i +=1
            curr_diag.sort()
            i = 0
            for j in range(k,n):
                grid[i][j] = curr_diag[i]
                i +=1
       
        return grid


        