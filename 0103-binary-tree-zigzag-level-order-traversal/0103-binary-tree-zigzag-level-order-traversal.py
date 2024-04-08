# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        hashTree = {}
        
        def dfs(node, level = 0):
            if node:
                if level in hashTree:
                    hashTree[level].append(node.val)
                else:
                    hashTree[level] = [node.val]
                    
                dfs(node.left, level + 1 )
                dfs(node.right, level + 1 )
        
        dfs(root)
        
        ans = []
        for i, nodes_level in hashTree.items():
            if i%2 == 0:
                ans.append(nodes_level)
            else:
                ans.append(nodes_level[::-1])

        return ans