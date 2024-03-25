# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', 
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        
        if l and r:
            return root
        else:
            return l or r
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # aproach create a function that build branch while finding node
        # compare branches until difer, retunr the node before defer
        
        
#         def findBranch(root,node_to_find):
#             ans = []
#             found = [False]
#             node = root
                
#             def findBranch_(node,node_to_find):
#                 if node and not found[0]:
#                     ans.append(node)
                    
#                     if node == node_to_find:
#                         found[0] = True
                
#                 if node.left: findBranch_(node.left,node_to_find)
                
                
#                 if node.right: findBranch_(node.right,node_to_find)
            
#             findBranch_(root,node_to_find)
#             return ans
        
#         branch_p = findBranch(root,q)
        
#         ans = []
#         for node in branch_p:
#             ans.append(node.val)
#         print(f"from {root.val} to {q.val}: {ans}")
        
        
        
#         return p
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        