# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # APROACH:
        # dfs saving the root to leaf path
        # cosntruct numbers and sum
        
        paths = []
        def dfs(node,path=[]):
            path.append(node.val)
            
            if not node.left and not node.right:
                paths.append(path)    
            if node.left:
                dfs(node.left,path.copy())
            if node.right:
                dfs(node.right,path.copy())
                
        def flatten_lists(lists):
            return [int(''.join(map(str, sublist))) for sublist in lists]
                
        dfs(root)
        paths = flatten_lists(paths) 

        return sum(paths)
            
                
                
            
            
            
            
            
        
        