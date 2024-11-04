# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #save nodes in list, if len(list) == k, reverse
        if k == 1:
            return head
        
        
        def reverse_nodes(sub_list):
            if  k == 2:
                temp = sub_list[2].next
                sub_list[2].next = sub_list[1]
                sub_list[1].next = temp
                sub_list[0].next = sub_list[2]         
                return sub_list[1]
                
            else:
                temp = sub_list[-1].next 
                for i in range(len(sub_list)-1,1,-1): 
                    sub_list[i].next = sub_list[i-1]
                sub_list[1].next = temp
                sub_list[0].next = sub_list[-1]
                return sub_list[1]
            
        
        
        
        def dfs(node,sub_list):
            if node:
                sub_list.append(node)
            
                temp = []
                for elem in sub_list:
                    temp.append(elem.val)
                print(temp)
            
                if len(sub_list) > k:
                    new_head = reverse_nodes(sub_list)
                    dfs(new_head,[])
                else:
                    dfs(node.next,sub_list)
            
                
        
        new_head = ListNode()
        new_head.next = head
    
        dfs(new_head,[])
        
        return new_head.next
        
        