class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        #brute force:

        n = len(grid)
        m = len(grid[0])

        min_i = 1001
        min_j = 1001
        max_i = -1
        max_j = -1

        for i in range(n):
            for j in range(m):
                if  grid[i][j] == 1:
                    min_i = min(min_i,i)
                    min_j = min(min_j,j)
                    max_i = max(max_i,i)
                    max_j = max(max_j,j)
    
        #print("i:",min_i,max_i,"j:",min_j,max_j,"area:",(max_j-min_j)*(max_i-min_j))

        return (max_j-min_j+1)*(max_i-min_i+1)

        
         







