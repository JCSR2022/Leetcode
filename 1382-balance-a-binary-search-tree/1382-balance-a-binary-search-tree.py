# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        
        #from https://www.youtube.com/watch?v=VqbP5isfJgE
        # time O(n), space O(n)
        
        
        inorder = []
        
        def traverse(node):
            if node is None:
                return
            
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
        
        
        def construct(left,right):
            if left > right:
                return None
            
         #   print(left,right,end=", ")
            
            if left == right:
         #       print(left == right,left,inorder[left])
                return TreeNode(inorder[left])

            mid = (left+right) //2
            current = TreeNode(inorder[mid])
         #   print(mid,inorder[mid])
            
            current.left  = construct(left,mid -1)
            current.right = construct(mid+1,right)
            
            return current
            
            
        traverse(root)
        #print(inorder)
        return construct(0,len(inorder)-1)
        
        
        


#never work ^$#$^$#&^%&%^^*U^&*&
#         nodes = []
#         def dfs(node):
#             if not node:
#                 return 
#             dfs(node.left)
#             nodes.append(node.val)
#             dfs(node.right)
            
#         def buildBalanceTree(new_nodes,father):
#             if not new_nodes:
#                 return
            
#             if len(new_nodes) == 1:
#                 if new_nodes[0] < father.val:
#                     father.left = TreeNode(new_nodes[0])
#                     return 
#                 else: 
#                     father.right = TreeNode(new_nodes[0])
#                     return 
            
            
#             print(new_nodes,father.val)
            
            
#             m = len(new_nodes)//2
            
#             new_node = TreeNode(new_nodes[m])
            
#             if new_nodes[m] < father.val:
#                 father.left = new_node
#             else: 
#                 father.right = new_node
                
#             buildBalanceTree(nodes[:m],new_node)
#             buildBalanceTree(nodes[m+1:],new_node)
        
        
#         dfs(root)
#         print(nodes)
        
#         m = len(nodes)//2
#         new_root = TreeNode(nodes[m])
#         buildBalanceTree(nodes[:m],new_root)
#         buildBalanceTree(nodes[m+1:],new_root)
        
#         return new_root
    
    
    
    
    
    
    
    
    
    
    
        
#         nodes = []
#         def dfs(node):
#             if not node:
#                 return 
#             dfs(node.left)
#             nodes.append(node.val)
#             dfs(node.right)
    
    
#         def buildBalanceTree(nodes):
#             m = len(nodes)//2
#             new_root = TreeNode(nodes[m])
            
#             node = new_root
#             for i in range(m-1,-1,-1):
#                 new_node = TreeNode(nodes[i])
#                 node.left = new_node
#                 node = new_node
                
#             node = new_root
#             for i in range(m+1,len(nodes)):
#                 new_node = TreeNode(nodes[i])
#                 node.right = new_node
#                 node = new_node
                
#             return   new_root
            
    
    
#         dfs(root)
        
#         print(nodes)
        
#         return buildBalanceTree(nodes)
    
    
    
        