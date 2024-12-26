# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        
        max_level_val = {}
        def dfs(node,level):
            if level in max_level_val:
                max_level_val[level] = max(max_level_val[level],node.val)
            else:
                max_level_val[level] = node.val

            if node.left: dfs(node.left,level+1)
            if node.right: dfs(node.right,level+1)
        
        
        if root:
            dfs(root,0)
            return list( max_level_val.values())
        
        return []
    
        #print(max_level_val)
        #return [ max_level_val[k]  k for sorted(max_level_val.keys())]
        
        
        
        
            
                
                
                
            
            
            
        