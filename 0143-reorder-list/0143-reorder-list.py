# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # aproach: 
        #    dfs linked list save nodes in a list
        #    move through list with 2 pointers, left and right
        #    until left > right change node.next 
        
        NodesList = []
        node = head
        while node:
            NodesList.append(node)
            node =node.next
        
        # special case:
        if len(NodesList) > 1:
   
            left = 0
            right = len(NodesList)-1

            ans = []
            while left < len(NodesList)//2:
                ans.append(NodesList[left])
                ans.append(NodesList[right])
                left +=1
                right -=1

            if  len(NodesList)%2 !=0:
                ans.append(NodesList[left])


            for i in range(len(ans)-1):
                ans[i].next = ans[i+1]
            ans[-1].next = None
        

        
        
            
            
            
            
            
            
            
            
            
            
        
        