# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        current = head

        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sums:
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != current:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next

        return dummy.next
        
        
#         curr = dummy = ListNode(0)
#         dummy.next = head
#         prefix = 0
#         seen = collections.OrderedDict()
        
#         while curr:
#             prefix += curr.val
#             if prefix not in seen:
#                 seen[prefix] = curr
#             else:
#                 node = seen[prefix]
#                 while list(seen.keys())[-1] != prefix:
#                     seen.popitem()
#             curr = curr.next
#         return dummy.next
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#         # fast with high use of memory:
#         # got trhu Listnode, safe node on dicc with values as keys and nodes as value
#         # every time find a negative value check if can be match with a key or a group of keys
#         # if  that can be done modify the adjacent nodes os that drop the nodes to be delete.
        
#         # Better:
#         # Got trhu Listnode, safe node.value in list
#         # work on list to eliminate values
#         # create new Listnode
        
#         returnList=[]
#         def goTrhuLinkedList(node):
#             if node:
#                 returnList.append(node.val)
#             if node.next:
#                 goTrhuLinkedList(node.next)
        
        
#         def eleminateSumZeroValues(arr):
#             """
#             sort the arr
#             two pointers L R 
#             while arr[L] < 0 and L<R   .....return arr[R,L]
#             i = R, find if -1*arr[L] <= sum(arr[i:R])
                
            
#             if -1*arr[L] == arr[:R]
#                 L = L+1
#                 R = i
#             else
            
#             NOOO NO PUEDES ORDENAR LA LISTA
#             """
#             pass
        
        
#         goTrhuLinkedList(head)
        
        
#         print(returnList)
        
#         return head
        
        
        