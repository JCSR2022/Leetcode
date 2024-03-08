# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        def dfs(node, currentSum):   
            currentSum += node.val
            print(node.val,currentSum)
            if not node.left and not node.right:
                return currentSum == targetSum

            isSumOnLeft = False
            isSumOnRight = False

            if node.left: 
                isSumOnLeft = dfs(node.left, currentSum)
            if node.right:
                isSumOnRight = dfs(node.right, currentSum)

            return isSumOnLeft or isSumOnRight

        return dfs(root, 0)