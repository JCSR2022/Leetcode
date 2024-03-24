# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # aproach time O(n), space O(n):
        # dfs build a list with the nodes in order 
        # change the left and right of each node
        
        
        list_nodes = []
        def dfs(node):
            if node:
                list_nodes.append(node)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        
        
        #special case:
        if not root:
            return root
        
        
        dfs(root)
        
        
        for i in range(len(list_nodes)-1):
            list_nodes[i].left = None
            list_nodes[i].right = list_nodes[i+1] 
        
        list_nodes[-1].left = None
        list_nodes[-1].right =None 
    
            
                
                
                
                
        