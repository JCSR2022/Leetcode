# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        

        ans = 0
        
        def dfs_postOrder(node):
            nonlocal ans
            
            if not node:
                return []
            
            leafs_left  = dfs_postOrder(node.left)
            leafs_rigth = dfs_postOrder(node.right)
            
                     
            if not node.left and not node.right: return [1]
            
            for l in leafs_left:
                for r in leafs_rigth:
                    if l+r <= distance:
                        ans += 1
            
            return [ 1+l for l in leafs_left ] + [1+r for r in leafs_rigth]
            
                
        dfs_postOrder(root)
        
        return ans
            