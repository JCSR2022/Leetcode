class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        # brute first aproach
        # for each row make the first bit 1 
        # for exah column check the numbers of 1 and if 0>1 then change
        #print(grid)
        
#         for row in grid:
#             if row[0] == 0:
#                 for i,bit in enumerate(row):
#                     if bit == 0:
#                         row[i] = 1
#                     else:
#                         row[i] = 0
#                 #print('1',grid)
            
#         for j in range(1,len(grid[0])):
#             sum_col = 0
#             for i in range(len(grid)):
#                 sum_col += grid[i][j]
#             #print('j',j,sum_col,len(grid)//2)
#             if sum_col <= len(grid)//2:
#                 for i in range(len(grid)):
#                     if grid[i][j] == 0:
#                         grid[i][j] = 1
#                     else:
#                         grid[i][j] = 0
#                 #print('2',grid)
        
        
#         def binario_a_decimal(row):
#             decimal = 0
#             for i, bit in enumerate(reversed(row)):
#                 decimal += bit * (2 ** i)
#             return decimal
        
#         sum_row = 0
#         for row in grid:
#             sum_row += binario_a_decimal(row)
                
#         return sum_row
        
            
#         Time complexity:
#         O(N^2)

#         Space complexity:
#         O(1)

        nRows, nCols = len(grid), len(grid[0])

        def flipRow(row):
            for col in range(nCols):
                grid[row][col] = 1 - grid[row][col] 

        def flipCol(col):
            for row in range(nRows):
                grid[row][col] = 1 - grid[row][col]

        def checkRow(nums):
            return int(''.join([str(num) for num in nums]), 2)
        
        for row in range(nRows):
            if grid[row][0] == 0:
                flipRow(row)
        for col in range(1, nCols):
            if sum(grid[r][col] for r in range(nRows)) * 2 < nRows:
                flipCol(col)
                
        return sum(checkRow(row) for row in grid)
    
    
    
    
    
    
                