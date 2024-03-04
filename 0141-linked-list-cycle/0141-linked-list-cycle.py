# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         # Brute force soluton Hash table
#         list_nodes = []
#         lisit_nodes_val =[]
        
#         def dfs(node):
#             if node:
#                 if node in list_nodes:
#                     return True
#                 else:
#                     lisit_nodes_val.append(node.val)
#                     list_nodes.append(node)
#                     return dfs(node.next)
#             else:
#                 return False
#         return dfs(head)


        # Two pointers :Floyd’s cycle finding or Hare-Tortoise algorithm

#         def FloydHareTortoise(nodeSlow, nodeFast):
#             if  (nodeSlow and 
#                 nodeFast and 
#                 nodeSlow.next and 
#                 nodeFast.next and
#                 nodeFast.next.next):
                    
#                 if nodeSlow == nodeFast:
#                     return True
#                 else:
#                     return FloydHareTortoise(nodeSlow.next, nodeFast.next.next)
#             else:
#                 return False
    
#         if head and head.next and head.next.next :
#             slow = head.next
#             fast = head.next.next

#             return FloydHareTortoise(slow, fast)
            
#         else:
#             return False      



        fast, slow = head, head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        
        return False
            
    
    
    
                
                
                
            
            
    
    
    
    
    
    
        