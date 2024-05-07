# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def traverse(node):
            if not node: return 0
            
            carry = traverse(node.next)
            #print('1:',node.val,carry,end=', ')
            
            total = node.val * 2 + carry
            
            node.val , carry = total%10 , total //10 
            
            #print('2:',node.val,carry,total)
            
            return carry
        
        carry = traverse(head)    
        
        if carry == 1:
            new_head = ListNode(carry)
            new_head.next = head
            return new_head
        
        return head
        