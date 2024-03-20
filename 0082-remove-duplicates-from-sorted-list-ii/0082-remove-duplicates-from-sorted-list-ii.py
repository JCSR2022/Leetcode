# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #aproach
        # move through list but only passing to the nex if nex is different than node
        
        # -100 <= Node.val <= 100 , so -200 will never be in Node.val
        dummy1 = ListNode(-101,head)
        dummy2 = ListNode(-200,dummy1)
        
        
        prev2Node = dummy2
        prev1Node = dummy1
        node = head
        
        
        while node:
            
            if prev1Node.val != node.val:
                prev2Node = prev1Node
                prev1Node = node
                node = node.next
                
            else:
                while node and prev1Node.val == node.val:
                    prev1Node = node
                    node = node.next
                
                prev2Node.next = node
                prev1Node = node
                if node: node = node.next
        
        return dummy1.next
        
        
        
        
        
        
        
        
        
        
#         while node:
#             print(prev2Node.val,prev1Node.val ,node.val, prev1Node.val == node.val)
            
#             if prev1Node.val != node.val:
#                 prev2Node = prev1Node 
#                 prev1Node = node
#                 node = node.next
#                 if node: print("p0:",prev2Node.val,prev1Node.val,node.val)
#             else:
#                 while prev1Node.val == node.val:
#                     print("p1:",prev2Node.val,prev1Node.val,node.val)
#                     prev1Node = node
#                     node = node.next
                
#                 prev2Node.next = prev1Node
#                 print("p2:",prev2Node.val,prev1Node.val,node.val)
       
    
#         return dummy1.next
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        