# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,leftLeaf):
            if not node.left and not node.right and leftLeaf:
                suma[0] += node.val
            if node.left: dfs(node.left,True)
            if node.right:dfs(node.right,False)
                
                
        suma = [0]
        dfs(root,False)
        return suma[0]
        
        