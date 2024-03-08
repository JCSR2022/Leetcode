# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
                
        valLevels = {}
        
        def dfs(node,level = 1):
            if node:
                if level in valLevels: 
                    valLevels[level].append(node.val)
                else:
                    valLevels[level] = [node.val]
            if node.left: dfs(node.left,level +1)
            if node.right: dfs(node.right,level +1)
            
        
        dfs(root)
        ans = []
        for arr in valLevels.values():
            ans.append(sum(arr) / len(arr))
        
        return ans
        
        