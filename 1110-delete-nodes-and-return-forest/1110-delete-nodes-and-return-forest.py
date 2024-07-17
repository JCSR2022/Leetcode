# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        

        
        # make dfs in reverse order so can delete nodes 
        
        deleted = []
        
        if root.val not in to_delete:
            deleted.append(root)
        
        def reverse_DFS(node,prev_node,r):
            if not node:
                return
            
            if node.left: reverse_DFS(node.left,node,False)
            if node.right: reverse_DFS(node.right,node,True)
            
            if node.val in to_delete:
                
                if node.left:   deleted.append(node.left)
                if node.right:  deleted.append(node.right)   
                
                if r: 
                    prev_node.right = None
                else:
                    prev_node.left  =  None
                
                
            
        dumy = TreeNode(None)   
        dumy.right = root    
        reverse_DFS(root,dumy,True)
        

        

        return deleted
        