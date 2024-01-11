# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        # Se exploran todas las ramas y se va almacenando el minimo y el maximo 
        # de la misma.
        
        self.ans = 0

        def buscador_min_max_rama(node,min_branch,max_branch):
            print(f"node:{node.val if node else 'null'}, min_rama:{min_branch},max_rama:{max_branch}",end="/")
            if not node:
                self.ans = max(self.ans, max_branch - min_branch)
                print(f"ans:{self.ans}")
                return
            
            min_branch = min(min_branch,node.val)
            max_branch = max(max_branch,node.val)
            
            print(f"Post: min_rama:{min_branch},max_rama:{max_branch}")
            
            buscador_min_max_rama(node.left,min_branch, max_branch)
            buscador_min_max_rama(node.right,min_branch, max_branch)
            
        buscador_min_max_rama(root,root.val,root.val)
        
        return self.ans
        
        
        