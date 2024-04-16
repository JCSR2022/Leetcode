# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        # make a dfs stop at depth and make the change
        
#         #special depth == 1
#         if depth == 1:
#             new_root = TreeNode(val)
#             new_root.left = root
#             return  new_root
        
        
#         def dfs(node,prev_node=None, level = 1,side=None):
            
#             if level == depth:
#                 new_node = TreeNode(val)
#                 if side == 'l':
#                     new_node.left = node
#                     prev_node.left = new_node
#                 elif side == 'r':
#                     new_node.right = node
#                     prev_node.right = new_node
                    
#             else:
#                 if node.left: dfs(node.left,node,level+1,side='l')
#                 if node.right: dfs(node.right,node,level+1,side='r')    
                
#         dfs(root)        
            
#         return root  
# THIS SOLUTION IS NOT GOOD, READ:Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.           

    
        # make a dfs stop at depth and make the change
        
        #special depth == 1
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return  new_root
        
        
        def dfs(node,level =1):
            
            if level == depth-1:
                
                l_node = TreeNode(val)
                r_node = TreeNode(val)
                
                l_node.left = node.left
                r_node.right = node.right
                
                node.left = l_node
                node.right = r_node
                     
            else:
                if node.left: dfs(node.left,level+1)
                if node.right: dfs(node.right,level+1)    
                
        dfs(root)        
            
        return root  
                