class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
  
        
  #-------------------------------
        #union find:
        roots = {}
        
        def find(x):
            if x not in roots:
                roots[x] = x
            while x != roots[x]:
                x = roots[x]
            return x
        
        def union(x,y):
            roots[find(x)] = find(y)
  #-------------------------------
                    
      # ---------
      # | \ U / |
      # |L \ / R|
      # |  / \  |
      # | / D \ |
      # ---------
        
        N = len(grid)
        for i in range(N):
            for j in range(N):            
                
                  # --------
                  # |  U /  |
                  # |L  / R |
                  # |  /    |
                  # | / D   |
                  # ---------  
                if grid[i][j] == "/":
                    union((i,j,'U'),(i,j,'L'))
                    union((i,j,'D'),(i,j,'R'))
                
                  # --------
                  # | \ U  |
                  # |L \  R|
                  # |   \  |
                  # |  D \ |
                  # ---------  
                elif grid[i][j]=="\\":
                    union((i,j,'U'),(i,j,'R'))
                    union((i,j,'D'),(i,j,'L'))
                                       
                  # --------
                  # |  U    |
                  # |L   R  |
                  # |       |
                  # |  D    |
                  # ---------  
                elif grid[i][j]==" ":
                        union((i,j,'U'),(i,j,'R'))
                        union((i,j,'D'),(i,j,'L'))  
                        union((i,j,'D'),(i,j,'U'))  
                
                  # ---------
                  # | \ U / |
                  # |L \ / R|
                  # |  / \  |
                  # | / D \ |
                  # | \ U / |
                  # |L \ / R|
                  # |  / \  |
                  # | / D \ |
                  # ---------
                if i > 0:
                    union((i-1,j,'D'),(i,j,'U'))
        
                  # ------------------
                  # | \ U /   \ U / |
                  # |L \ / R L \ / R|
                  # |  / \     / \  |
                  # | / D \   / D \ |
                  # -----------------
                if j > 0:
                    union((i,j-1,'R'),(i,j,'L'))
        
        return len(set(map(find,roots)))
        
        
        
        
        
        
        
        
        
        
        
        