# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
    
        def dfs(node,bin_num):

            bin_num.append(node.val)

            if node.left and node.right:
                left = dfs(node.left,bin_num)
                right = dfs(node.right,bin_num)
                bin_num.pop()
                return left + right
            elif node.right:
                right = dfs(node.right,bin_num)
                bin_num.pop()
                return right
            elif node.left:
                left = dfs(node.left,bin_num)
                bin_num.pop()
                return left
            else:
                ans = sum([ n*(2**i) for i,n in enumerate(bin_num[::-1])]) 
                bin_num.pop()
                return ans

        return dfs(root,[])
        