# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS
        def compareTree(node_p, node_q):
            if not node_p and not node_q:
                return True
            elif not node_p or not node_q:
                return False
            else:
                if node_p.val != node_q.val:
                    return False

                return compareTree(node_p.left, node_q.left) and compareTree(node_p.right, node_q.right)

        return compareTree(p, q)
            