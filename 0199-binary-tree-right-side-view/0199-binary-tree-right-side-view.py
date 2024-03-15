# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if not root:
            return root
        
        valuesLevels = {}
        
        def nodesInlevels(node,level = 0):
            
            if level in valuesLevels:
                valuesLevels[level].append(node.val)
            else:
                valuesLevels[level] = [node.val]
            
            if node.left: nodesInlevels(node.left,level+1)
            if node.right: nodesInlevels(node.right,level+1)
            
            
            
        nodesInlevels(root)
        
        ans = []
        
        for level,values in valuesLevels.items():
            ans.append(values[-1])
        
        return ans
                
        
        