# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node,pre_node = None, left=None):
            
            if node.left: dfs(node.left,node,True)
            if node.right: dfs(node.right,node,False)

            if not node.left and not node.right:
                if node.val == target:
                    if pre_node:
                        if left == True:
                            pre_node.left = None
                        else:
                            pre_node.right = None
                    else:
                        node.val = None

                        
                        
        dfs(root)
        
        if not root.val:
            return None
        
        return root
                    
                    
            
        