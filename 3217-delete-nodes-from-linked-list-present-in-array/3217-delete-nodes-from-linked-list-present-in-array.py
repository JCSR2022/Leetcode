# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        

        nums =set(nums)
        new_head = ListNode()
        curr_node = new_head
 
        while True:

            if head.val not in nums:
                curr_node.next = head
                curr_node = curr_node.next
     
            if head.next:
                head = head.next
            else:
                break

        return new_head.next
        

































        #create dummyhead use as head
        #dfs remove nodes if  in list
        
#         nums = set(nums)
    
#         def dfs(prev_node,node):
#             if not node:
#                 return
            
#             if node.val in nums:
#                 prev_node.next = node.next
#             else:
#                 prev_node = node
    
#             dfs(prev_node,node.next)
    
    
#         dummy = ListNode(None,head)
#         dfs(dummy ,head)
        
#         return dummy.next


# #----------------------------------------------------

#         dummy = node = ListNode(next = head)
#         set_nums = set(nums)
#         while node.next:
#             if node.next.val in set_nums:
#                 node.next = node.next.next
#             else:
#                 node = node.next
#         return dummy.next     



