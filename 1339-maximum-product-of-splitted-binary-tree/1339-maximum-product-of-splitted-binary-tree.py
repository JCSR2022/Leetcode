# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        # aproach:
        # find total sum, make dfs @#$@#$

        MOD = 10**9+7


        def dfs_sum(node):

            left = 0
            right = 0

            if node.left:
                left = dfs_sum(node.left)
            if node.right:
                right = dfs_sum(node.right)
            
            return node.val + left + right



        total = dfs_sum(root)
        #print("Total:",total)
        max_val = [0] 
        def dfs_split(node):
            left = 0
            right = 0

            if node.left:
                left = dfs_split(node.left)
            if node.right:
                right = dfs_split(node.right)
            
            curr_val = node.val + left + right
            
            max_val[0] = max(max_val[0],curr_val*(total-curr_val))
            #print(curr_val,total-curr_val,curr_val*(total-curr_val)  , max_val[0])

            return curr_val

        dfs_split(root)

        return max_val[0]%MOD
        






        