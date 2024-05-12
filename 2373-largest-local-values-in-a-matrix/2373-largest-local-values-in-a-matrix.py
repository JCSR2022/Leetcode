class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        #brute force:
        
        n = len(grid)-2    
        
        def findMax(l,r,u,d):
            #print("l,r,u,d",l,r,u,d)
            
            val_max = float("-inf")
            for i in range(u,d+1):
                for j in range(l,r+1):
                    #print(i,j,grid[i][j],val_max)
                    val_max = max(val_max,grid[i][j])
            #print('val_max:',val_max)
            
            return val_max
    
    
    
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        for row in range(n):
            for col in range(n):
                #print('row,col',row,col)
                ans[row][col] = findMax(col,col+2,row,row+2)
                #print(ans)
        
        return ans
        
        
        
        