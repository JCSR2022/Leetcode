# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        #1. def is critical(node) find critical point return true or false
        #  dfs if critical safe pos in arr
        
        
        def iscritical(pre_node,node):
            if node.next:
                # minimum
                if pre_node.val > node.val and node.next.val > node.val:
                    return True
                # maximum
                if pre_node.val < node.val and node.next.val < node.val:
                    return True
            return False
            
            
        cont  =  0
        min_dist = float('inf')
        first = -1
        actual = -1
        
        pre_node = head
        node = pre_node.next
        
        while node:
            if iscritical(pre_node,node):
                
                if first == -1:
                    first = cont
                    
                if actual != -1:
                    min_dist = min(min_dist,cont-actual)
                actual = cont
    
            pre_node = node
            node = node.next
            cont +=1
        
        
        if min_dist <float('inf'):
            max_dist = actual-first
            return [min_dist,max_dist]
        else:
            return [-1,-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #1. def is critical(node) find critical point return true or false
#         #  dfs if critical safe pos in arr
        
#         def iscritical(pre_node,node):
#             if node.next:
#                 # minimum
#                 if pre_node.val > node.val and node.next.val > node.val:
#                     return True
#                 # maximum
#                 if pre_node.val < node.val and node.next.val < node.val:
#                     return True
#             return False
            
            
#         cont  =  0
#         criticals = []
#         pre_node = head
#         node = pre_node.next
        
#         while node:
#             if iscritical(pre_node,node):
#                 criticals.append(cont)
#             pre_node = node
#             node = node.next
#             cont +=1
        
#         #print(criticals)
        
#         if len(criticals) < 2:
#             return [-1,-1]
        
#         min_dist = float('inf')
#         for i in range(len(criticals)-1):
#             min_dist = min(min_dist,criticals[i+1]-criticals[i])
            
#         max_dist = criticals[-1]-criticals[0]
        
#         return [min_dist,max_dist]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        