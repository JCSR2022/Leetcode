# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dfs on chain , create a new linked list, O(n) time
        
#         node = head.next
#         new_head = ListNode()
#         new_node = new_head
#         suma = 0
        
#         while node:
                
        
        
        node = head.next
        node0 = head
        suma = 0
        
        while node:
            #print(node.val,suma)
            if node.val == 0:
                node0.val = suma
                node0.next = node.next
                node0 = node0.next
                node = node.next
                suma = 0
            else:
                suma += node.val
                node = node.next
        
        return head
        