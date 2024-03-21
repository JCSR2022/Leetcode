# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # dfs prev_node and node, change next to previus
        
        #specials case:
        if not head:
            return head
        
        if not head.next:
            return head
        
        node = head.next
        prev = head
        prev.next = None
        
        while node.next:
            temp = node.next
            node.next = prev
            
            prev = node
            node = temp
            
        node.next = prev
        return node
            
        
        
            
            
            
            
            
            
            
        