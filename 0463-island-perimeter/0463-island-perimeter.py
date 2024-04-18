class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #solve O(n*m)  formaly O(n)
        
        n = len(grid)
        m = len(grid[0])
        
        def check_perimeter(i,j):
            if i > n-1 or j > m-1  or i<0 or j<0:
                raise f"error en los limites {i,j}"
            perimeter = 0
            
            # check left:
            if j == 0 : 
                perimeter += 1
            else: 
                if grid[i][j-1] == 0: perimeter += 1 
            
            # check right:
            if j == m-1: 
                perimeter += 1
            else: 
                if grid[i][j+1] == 0: perimeter += 1 
            
            #check up:
            if i == 0: 
                perimeter += 1
            else: 
                if grid[i-1][j] == 0: perimeter += 1
                    
            #check down:
            if i == n-1: 
                perimeter += 1
            else: 
                if grid[i+1][j] == 0: perimeter += 1
            
            return perimeter
                
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    p = check_perimeter(i,j)
                    ans += p 
                    #print(i,j,p,ans)
        return ans
            
            
            
        