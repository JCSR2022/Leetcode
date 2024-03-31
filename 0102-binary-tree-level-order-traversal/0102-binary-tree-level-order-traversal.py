# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashleveles = {}
        def dfs(node,hashleveles,level =0):
            if node:
                if level in hashleveles:
                    hashleveles[level].append(node)
                else:
                    hashleveles[level] = [node]
                
                dfs(node.left,hashleveles,level+1)
                dfs(node.right,hashleveles,level+1)
            
        dfs(root,hashleveles) 
        
        ans =[]
        for levelnodes in hashleveles.values():
            nodes = [node.val for node in levelnodes]
            ans.append(nodes)
        
        return ans
            