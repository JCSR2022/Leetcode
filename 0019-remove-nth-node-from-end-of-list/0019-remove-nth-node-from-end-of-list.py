# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #dfs? hashtable?  time : O(n), space: O(n) 
        
#         next_vector = [head]
        
#         def create_node_next_list(node):
#             while node.next:
#                 next_vector.append(node.next)
#                 node = node.next

            
#         create_node_next_list(head)
        
#         if len(next_vector) == 1:
#             head.val = ""
            
#         elif len(next_vector) == n:
#             head = head.next
            
#         else:
#             next_vector[-n-1].next = next_vector[-n].next
        
#         return head


        # Two Pointer time O(n) space O(1)

        dummy = ListNode(None,head)
        left = dummy
        right = head
        
        
        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        
        return dummy.next
    
    