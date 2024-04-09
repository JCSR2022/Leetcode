# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        # if you do a dfs In-order you will obtane the order tree
        
        tree = []
        
        def dfs_InOrder(node):
            if node.left: dfs_InOrder(node.left)
            tree.append(node.val)
            if node.right: dfs_InOrder(node.right)
        
        
        dfs_InOrder(root)   
        print(tree)
        return tree[k-1]