# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #null sol
        if not root:
            return 0
        
        maxLevel = 0
        
        def dfs(node,level = 1):
            nonlocal  maxLevel
            
            maxLevel = max(maxLevel,level)
            
            if node.left : dfs(node.left,level+1)
            if node.right : dfs(node.right,level+1)
        
        dfs(root)
        
        return maxLevel
                
            
            
        