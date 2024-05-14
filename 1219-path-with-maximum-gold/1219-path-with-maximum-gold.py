class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        #dp = [ [0]*len(grid[0]) for _ in range(len(grid))]
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r,c,visit=set()):
            if ( min(r,c) < 0 or r >= rows or c >= cols or
                 grid[r][c] ==0 or
                 (r,c) in visit):
                return 0
            
            visit.add((r,c))
            ans = grid[r][c]
            
            neighbors = [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            
            for neig_r,neig_c in neighbors:
                ans = max(ans, grid[r][c] + dfs(neig_r,neig_c,visit))
            
            visit.remove((r,c))
            
            return ans
            

        res = 0
        
        for r in range(rows):
            for c in range(cols):
                res = max(res,dfs(r,c))
          
        
    
        return res
        
        
        
        
        
        
        
        
        
        
        
        