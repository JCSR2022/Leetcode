class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        #brute force, find all paths

        Mod = 10**9+7
        
        m = len(grid)
        n = len(grid[0])

        my_memory = {}
        def dfs(i,j,curr_sum):
            
            if (i,j,curr_sum) in my_memory:
                return my_memory[(i,j,curr_sum)]

            if i==m-1 and j==n-1:
                curr_sum += grid[i][j] 
                if curr_sum%k == 0:
                    return 1
                else:
                    return 0
            
            path1 = 0
            path2 = 0
            if i < m-1:
                path1 = dfs(i+1,j,(curr_sum+grid[i][j])%k)
            if j < n-1:
                path2 = dfs(i,j+1,(curr_sum+grid[i][j])%k)
            
            my_memory[(i,j,curr_sum)] = (path1+path2)%Mod

            return my_memory[(i,j,curr_sum)]

        return dfs(0,0,0)

#Time Limit Exceeded
#---------------------------------------------