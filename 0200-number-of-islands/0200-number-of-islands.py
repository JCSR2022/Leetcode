class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Aproach
        #   BFS until found a 1, then DFS mark all adyacent land 
        #   when found 1 cont islands +=1 , change "1" for 'c' of check
        
        
        def dfs_island(i,j):
            if grid[i][j] == '1':
                
                grid[i][j] = 'c'
            
                #check up
                if i > 0: dfs_island(i-1,j)

                #check down
                if i < len(grid)-1: dfs_island(i+1,j)
                    
                #check left
                if j > 0: dfs_island(i,j-1)
                
                #check right
                if j < len(grid[0])-1:  dfs_island(i,j+1)
            
                
        
        count_island = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count_island +=1
                    dfs_island(i,j)
        
        #print(grid)
                
        return count_island
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not grid:
#             return 0
        
#         def dfs(i,j):
#             if grid[i][j] == "1":

#                 grid[i][j] = "L"
          
#                 if i > 0:              dfs(i-1,j)  # move up
#                 if i < len(grid)-1:    dfs(i+1,j)  # move down
#                 if j > 0:              dfs(i,j-1)   # move left
#                 if j < len(grid[0])-1: dfs(i,j+1)  # move right

#             else:
#                 return

#         rows = len(grid)
#         cols = len(grid[0])
#         islands = 0

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1":
#                     islands +=1
#                     dfs(r,c)
        
#         return islands
            
        