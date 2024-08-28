class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        #1. find match between grid1 and grid2, identify as 2 o grid2
        #2. check if islands of 2 have only 0 arround
        
        m = len(grid1)
        n = len(grid1[0])
        
        
        for i in range(m):
            for j in range(n):
                if grid1[i][j] and grid2[i][j]:
                    grid2[i][j] = 2
                grid1[i][j] = 0
        
        print(grid1)
        print(grid2)
        
        def dfs(i,j):

            if  grid1[i][j] != 1 and grid2[i][j] == 2:
                grid1[i][j] = 1 #visited
            else:
                return False

            up,down,left,right = True,True,True,True

            if i-1 >= 0 and grid1[i-1][j] !=1 and grid2[i-1][j] != 0 : up = dfs(i-1,j)

            if i+1 < m and grid1[i+1][j] !=1 and grid2[i+1][j] != 0: down = dfs(i+1,j)

            if j - 1 >=0 and grid1[i][j-1] !=1 and grid2[i][j-1] != 0:  left = dfs(i,j-1)

            if j + 1 < n and grid1[i][j+1] !=1 and grid2[i][j+1] != 0: right = dfs(i,j+1)  

            return up and down and left and right

        
        ans =0
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j):
                    ans +=1
        
        return ans
        