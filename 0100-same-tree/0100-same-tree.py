# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # El CDTM JAJAJAJA
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
        
        #yo
#         if not p and not q:
#             return True
#         elif not p or not q:
#             return False
#         else:
#             if p.val != q.val:
#                 return False
#             return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)
        

            