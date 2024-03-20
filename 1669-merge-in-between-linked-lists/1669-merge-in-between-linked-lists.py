# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        # aproach:
        # find a node 
        # find b + 1 node
        # change a_node.next to point list2
        # change last node in list2 to poitn b+1 node 
        
#         a_node = []
#         b_plus1_node = []
#         last_node_list2 =[]
        
#         # finding a_node and b+1 node
#         node = list1
#         cont = 1
#         while node:
#             #print(node.val,cont)
#             if cont == a:
#                 a_node.append(node)
#             if cont == b+1:
#                 b_plus1_node.append(node.next)
#                 break
#             node = node.next
#             cont +=1
   
#         # find last node on list2
#         node = list2
#         while node:
#             if not node.next:
#                 last_node_list2.append(node)
#             node = node.next
        
#         # Doing changes:
        
#         a_node[0].next = list2
#         last_node_list2[0].next = b_plus1_node[0]
        
 
#         return list1    




        a_node = None
        b_plus1_node = None
        last_node_list2 = None 
        
        
        # finding a_node and b+1 node
        node = list1
        cont = 1
        while node:
            #print(node.val,cont)
            if cont == a:
                a_node = node
            if cont == b+1:
                b_plus1_node =node.next
                break
            node = node.next
            cont +=1
   
        # find last node on list2
        node = list2
        while node:
            if not node.next:
                last_node_list2 = node
            node = node.next
        
        # Doing changes:
        
        a_node.next = list2
        last_node_list2.next = b_plus1_node
        
 
        return list1    
            
    
    
    
    
    
    
    
        