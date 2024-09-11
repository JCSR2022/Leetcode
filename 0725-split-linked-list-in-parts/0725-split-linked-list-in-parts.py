# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

    
        node = head
        cont = 0
        while node:
            cont += 1
            node = node.next    
        pre_ans = [cont//k]*k 
        for i in range(cont%k):
            pre_ans[i] += 1
            
            
            
        print(pre_ans)

        
        def create_chunk(chunk,size):
            
            while size > 1:
                size -= 1
                if chunk.next:
                    chunk = chunk.next
                
            next_chunk = chunk.next
            chunk.next = None
            return next_chunk
        
        node = head
        ans =[None]*k
        for i,size in enumerate(pre_ans):
            if size != [] and node:
                ans[i] = node
                node = create_chunk(node,size)
        return ans
        
        
        
        
            
        # ans = []
        # inic = 0 
        # for num in pre_ans:
        #     ans.append(list_head[inic:inic+num])
        #     inic += num

        return head

        
        
        
        
        
        
        
        
        
        
#         ans = [None] * k

#         # Calculate total size of the linked list
#         size = 0
#         current = head
#         while current:
#             size += 1
#             current = current.next

#         # Minimum size of each part
#         split_size = size // k
#         remainder = size % k  # Remaining nodes to distribute

#         current = head
#         for i in range(k):
#             ans[i] = current
#             current_size = split_size + (1 if remainder > 0 else 0)
#             remainder -= 1

#             # Traverse to the end of the current part
#             for _ in range(current_size - 1):
#                 if current:
#                     current = current.next

#             # Cut the list
#             if current:
#                 next_part = current.next
#                 current.next = None
#                 current = next_part

#         return ans