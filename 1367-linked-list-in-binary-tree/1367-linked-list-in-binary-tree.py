# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #$^#$^#$^#^#$^no funciona
    
    # def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            
#         def check(tree_node,list_node):
            
#             if list_node is None:
#                 #print("found")
#                 return True
            
#             #print(tree_node.val,list_node.val)

#             left = False
#             right = False
            
#             if tree_node.val == list_node.val:
                
#                 if tree_node.left:
#                     left = check(tree_node.left,list_node.next)

#                 if tree_node.right:
#                     right = check(tree_node.right,list_node.next)

            
#             return  left or right 
                
     
            
            
#         def dfs(tree_node):
#             #print("## :",tree_node.val)
            
#             left =False
#             right = False
#             actual = False
            
#             if tree_node:
#                 actual = check(tree_node,head)
                
#             if tree_node.left:
#                 left = check(tree_node.left,head)
    
#             if tree_node.right:
#                 right = check(tree_node.right,head)
        
#             return actual or right or left
            
        
#         return dfs(root)
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    def dual_dfs(self,list_node, tree_node):
    
            if not list_node:
                return True
            
            if not tree_node or list_node.val != tree_node.val:
                return False

            return self.dual_dfs(list_node.next, tree_node.left) or self.dual_dfs(list_node.next, tree_node.right) 
    
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        
        if self.dual_dfs(head,root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right) 


        
        
        
        
        
        # me dfs moving with head also, save list of nodes visited and check if new node match
               
#         def dual_dfs(head_node,tree_node,new_review=True):
            
#             if  new_review: 
#                 if head_node.val == tree_node.val:
#                     new_review = False
#                     next_head_node = head_node.next
#                 else:
#                     next_head_node = head_node
                
#             else:
#                 if head_node.val == tree_node.val:
#                     next_head_node = head_node.next
#                 else:
#                     if tree_node.val == head.val:
#                         new_review = False
#                         next_head_node = head.next
#                     else:
#                         new_review = True
#                         next_head_node = head
 
#             if next_head_node == None:
#                 return True
            
            
#             if tree_node.left:
#                 if dual_dfs(next_head_node,tree_node.left,new_review):
#                     return True
                
#             if tree_node.right:
#                 if dual_dfs(next_head_node,tree_node.right,new_review):
#                     return True
            
#         if dual_dfs(head,root):
#             return True
#         else:
#             if root.left:
#                 if self.isSubPath(head,root.left): return True
#             if root.right:
#                 if self.isSubPath(head,root.right): return True
        
#         return False
                
                      
            
            
        