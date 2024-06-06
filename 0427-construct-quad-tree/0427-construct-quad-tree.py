"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        # Brute force wost case aproach n**2 
        
        
        # botoom to top aproach T = n
        
        def isValuesSame(grid,tl,br):
            """
            find is values are the same on a submatrix of grid where
            tl = is the top left corner (i,j) coordenate
            br = is the bootom right corner (i,j) coordenate
            """
            val = grid[tl[0]][tl[1]]
            for i in range(tl[0],br[0]):
                for j in range(tl[1],br[1]):
                    if not grid[i][j] == val:
                        return False
            return True
        
        
        def dfs(grid,r,c,n):
            
            tl = [r,c]
            br = [r+n,c+n]
            
            
            if isValuesSame(grid,tl,br):
                return Node(grid[r][c],True)
            
            topLeft = dfs(grid,r,c,n//2)
            topRight = dfs(grid,r,c+n//2,n//2)
            bottomLeft = dfs(grid,r+n//2,c,n//2)
            bottomRight = dfs(grid,r+n//2,c+n//2,n//2)
            return Node(None,False,topLeft,topRight,bottomLeft,bottomRight)

        root = dfs(grid,0,0,len(grid))
        
        # nodeExamp1 = Node(1,True)
        # nodeExamp2 = Node(0,True)
        # root = Node(None,False,nodeExamp1,nodeExamp2,nodeExamp2,nodeExamp1)
        # print(isValuesSame(grid,tl,br))
        
        return root
             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        