class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
#         #sol from top to bootom 
#         dp = [ [0]*len(grid[0]) for _ in grid ]

#         def find_min(i,j):
#             if i == 0 and j == 0:
#                 return 0
#             if i == 0 and j > 0:
#                 return dp[i][j-1]    
#             if i > 0 and j == 0:
#                 return dp[i-1][j]
#             return min(dp[i-1][j],dp[i][j-1])


#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 dp[i][j] = grid[i][j] + find_min(i,j)
                
#         return dp[-1][-1]



    
        # sol bootom to top
        
        rows = len(grid)
        cols = len(grid[0])
        
        res = [[float("inf")]*(cols+1) for r in range(rows+1)]
        res[rows-1][cols] = 0 
        
        
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                res[r][c] = grid[r][c]+ min(res[r+1][c],res[r][c+1])
                
        return res[0][0]
        
        
        
        
        
        
        

        