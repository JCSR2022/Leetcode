# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # note: very good explination:
        # https://www.youtube.com/watch?v=ihj4IQGZ2zc
        
        # aproach: 
        
        # note: this can be solve only because
        #        "preorder and inorder consist of unique values"
        # first value on preorder is the root (always)
        
        
        # end of recursive
        if not preorder or not inorder:
            return None
        

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # recursion
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:] , inorder[mid+1:])
        
        return root
        
        