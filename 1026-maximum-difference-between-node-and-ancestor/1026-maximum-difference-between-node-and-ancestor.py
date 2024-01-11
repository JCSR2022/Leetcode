# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def buscador_min_max_rama(node,min_branch,max_branch):
            if not node:
                self.ans = max(self.ans, max_branch- min_branch)
                return
            
            min_branch = min(min_branch,node.val)
            max_branch = max(max_branch,node.val)
            
            buscador_min_max_rama(node.left,min_branch, max_branch)
            buscador_min_max_rama(node.right,min_branch, max_branch)
            
        buscador_min_max_rama(root,root.val,root.val)
        
        return self.ans
        
        
        