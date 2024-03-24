# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        # aproach: dfs saving a count for the nodes on the highest level (maxLevel)
        # then calculate sum([2**n for n in range(maxLevel-1)]) + nodes on maxLevel 

        maxLevel = [0]
        nodesOnMaxLevel = [0]
        
        def dfs(node,level = 1):
            if node:
                if level > maxLevel[0]:
                    maxLevel[0] = level
                    nodesOnMaxLevel[0] = 1
                    
                elif level == maxLevel[0]:
                    nodesOnMaxLevel[0]  += 1
                    
                if node.left: dfs(node.left,level + 1)
                if node.right: dfs(node.right,level + 1)
                    
        dfs(root)
        nodesOnOtherLevels = sum([2**n for n in range(maxLevel[0]-1)])
        
        
        print( nodesOnMaxLevel[0],nodesOnOtherLevels )
        
        
        return  nodesOnOtherLevels+ nodesOnMaxLevel[0]
                
                    
                    
                
                
     
            
            
        
        