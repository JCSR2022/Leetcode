# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        def walk_true(node):
            if node.left or node.right:
                if node.left:
                    walk_true(node.left)
                if node.right:
                    walk_true(node.right)
            else:
                self.root_leaf = self.root_leaf+[node.val]

        self.root_leaf = []
        walk_true(root1)
        root1_leaf = self.root_leaf
        print(root1_leaf)

        self.root_leaf = []
        walk_true(root2)
        root2_leaf = self.root_leaf
        print(root2_leaf)

        return root1_leaf == root2_leaf


        


        

            





        