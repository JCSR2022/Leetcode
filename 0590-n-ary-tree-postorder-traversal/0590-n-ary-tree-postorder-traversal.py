"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        
        ans = []
        def dfs_postorder(node):
            if node.children:
            
                for child in node.children:
                    dfs_postorder(child)
                    ans.append(child.val)    

        
        dfs_postorder(root)
        ans.append(root.val)

        return ans