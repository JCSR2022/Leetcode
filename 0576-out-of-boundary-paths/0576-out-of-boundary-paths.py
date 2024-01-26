class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        
        # Down, Up, Right, Left
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        @lru_cache(None)
        def dp(i,j,moves):
            
            if i<0 or j<0 or i>=m or j>=n:
                return 1
            
            if moves == 0:
                return 0
            
            ans = 0 
            
            for d in directions:
                ni = i + d[0]
                nj = j + d[1]
                ans += dp(ni,nj,moves-1)
            
            return ans
        
        result = dp(startRow,startColumn,maxMove)
        
        return result % (10**9 + 7)
                
            
        