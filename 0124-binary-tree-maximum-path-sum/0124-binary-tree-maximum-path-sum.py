# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        #aproach dynamic programing , billd adjance matrix with path sum
        #def dfs_buld_adjance_matrix(node,level):
        #noooooooooooooooooooooooooooooooooo
        
#-----------------------------------------------------------------

        ans = float("-inf")
    
        def dfs_find_max(node):
            
            nonlocal ans
            
            if node:
            
                left =  max(dfs_find_max(node.left),0)
                right = max(dfs_find_max(node.right),0)
                ans = max(ans, node.val+left+right )
            
                return max(left,right,0) + node.val
                
            else:
                return 0
        
        
        dfs_find_max(root)
        
        return ans
            
            
        