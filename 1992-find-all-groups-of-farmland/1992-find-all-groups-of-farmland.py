class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        
        # bfs until 1, then dfs safe i,j and cheking if no left and down safe i,j
        
        
        
        def dfs_corners(i,j,left_up_corner=False):
            
            nonlocal corners
            
            #print(land,i,j,corners)
            
            land[i][j] = 2   # means check
            
            
            if not left_up_corner:
                corners = [0,0,0,0]
                corners[0] = i
                corners[1] = j
            
            corners[2] = max(corners[2],i)
            corners[3] = max(corners[3],j)
  
            # check right:
            if j < len(land[0])-1 and land[i][j+1] == 1 : dfs_corners(i,j+1,True)
                    
            # check down:
            if i < len(land)-1 and land[i+1][j] == 1 : dfs_corners(i+1,j,True)

        
        ans = []
        corners = [0,0,0,0]
        
        for i in range(len(land)):
            for j in range(len(land[0])):
                #print(i,j,land,ans)
                if land[i][j] == 1:
                    dfs_corners(i,j)
                    ans.append(corners)
            
        return ans