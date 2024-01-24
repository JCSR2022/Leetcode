# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = 0
        
        def dfs(node):
            nonlocal odd
            if not node:
                return 0
            
            count[node.val] +=1
            odd_change = 1 if count[node.val] % 2 == 1 else -1
            odd += odd_change
            
            if not node.left and not node.right:
                ans = 1 if odd <= 1 else 0 
            else:
                ans = dfs(node.left)+ dfs(node.right)
            odd -= odd_change 
            count[node.val] -=1
            return ans
        
        return dfs(root)
            
        