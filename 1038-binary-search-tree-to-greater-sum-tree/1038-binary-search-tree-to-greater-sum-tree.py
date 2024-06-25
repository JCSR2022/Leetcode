# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        current_sum = 0
        
        def reverseDFS(node):
            if not node:
                return
            
            nonlocal current_sum
            
            reverseDFS(node.right)
            temp = node.val
            node.val += current_sum
            current_sum += temp
            
            reverseDFS(node.left)
            
        reverseDFS(root)
        
        return root