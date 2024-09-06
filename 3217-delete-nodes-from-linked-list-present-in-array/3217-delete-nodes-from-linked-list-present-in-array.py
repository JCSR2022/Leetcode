# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        #create dummyhead use as head
        #dfs remove nodes if  in list
        
        nums = set(nums)
    
        def dfs(prev_node,node):
            if not node:
                return
            
            if node.val in nums:
                prev_node.next = node.next
            else:
                prev_node = node
    
            dfs(prev_node,node.next)
    
    
        dummy = ListNode(None,head)
        dfs(dummy ,head)
        
        return dummy.next