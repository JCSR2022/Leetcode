class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
#         # brute force:
#         pos = []
        
        
#         i = 0
#         j_ant = 0
        
#         nexts = [j for j in range(len(grid[0])) if j != j_ant ]
#         print(nexts)
        
#         while i<len(grid):
#             i += 1
#             for j in next:
#             print(j,[j for j in range(len(grid[0])) if j != j_ant ])
#             next = 
        
                
#         return 0
                    
                  
        dp = [ [0]*len(grid[0]) for _ in range(len(grid)) ]
        
        dp[0] = grid[0]
        
        
        for i in range(1,len(grid)):
            for j in range(0,len(grid[0])):
                dp[i][j] = min(dp[i-1][:j]+dp[i-1][j+1:])+grid[i][j]
                
        
        print(dp)
        
        return min(dp[-1])
            
            

            
        
        
        
        