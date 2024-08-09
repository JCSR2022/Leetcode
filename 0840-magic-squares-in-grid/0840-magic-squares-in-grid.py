class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        #brute force move through the gird, check if magic squarÑ
        
#         rows = len(grid)
#         columns = len(grid[0])
        
#         def is_magic_square(i,j):
#             nonlocal rows,columns
        
#             if i >= 0 and i+2 < rows and j >=0 and j+2 < columns:
                
#                 nums = set()
#                 for x in range(i,i+3):
#                     for y in range(j,j+3):
#                         nums.add(grid[x][y])
#                 cond_2 = nums == set(range(1,10)) 
                
                
#                 sum_diag_1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
#                 sum_diag_2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
#                 cond_3 =  sum_diag_1 == sum_diag_2
                
#                 print(cond_2,cond_3)
                
#                 if cond_2 and cond_3:
#                     return True                
            
#             return False
        
#         cont = 0
#         for i in range(rows):
#             for j in range(columns):
            
#                 if is_magic_square(i,j):
#                     cont +=1
                    
#         return cont




        def check(i, j):
            
            sums = []
            visited = set()
            for ii in [-1, 0, 1]:
                for jj in [-1, 0, 1]:
                    if grid[ii+i][jj+j] in range(1, 10):
                        visited.add(grid[ii+i][jj+j])
            
            if len(visited) != 9:
                return False
            
            sums.append(grid[i][j] + grid[i][j+1] + grid[i][j-1])
            sums.append(grid[i-1][j] + grid[i-1][j+1] + grid[i-1][j-1])
            sums.append(grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j-1])
            sums.append(grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1])
            sums.append(grid[i-1][j] + grid[i][j] + grid[i+1][j])
            sums.append(grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1])
            sums.append(grid[i][j] + grid[i+1][j-1] + grid[i-1][j+1])
            sums.append(grid[i][j] + grid[i+1][j+1] + grid[i-1][j-1])

            for i in range(1, 8):
                if sums[i-1] != sums[i]:
                    return False
            return True
        
        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(1, m-1):
            for j in range(1, n-1):
                if check(i,j):
                    res += 1
        
        return res