# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dfs creting two new linked list at the end join
        
        dummy1 = ListNode()
        dummy2 = ListNode()
        
        node = head
        leftNodes = dummy1
        rightNodes = dummy2
        
        while node:
            if node.val < x:
                leftNodes.next = node
                leftNodes = leftNodes.next 
            else:
                rightNodes.next = node
                rightNodes = rightNodes.next
            node = node.next
        
        
        leftNodes.next = dummy2.next
        rightNodes.next = None
        
        return dummy1.next
        
        