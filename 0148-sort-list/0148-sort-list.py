# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # aproach: make a hashMap with nodes a values , sort by values
        # change next in each node to point to node in order
        # Sol time: O(n logn) for the sort() algorithm , space O(n) 
        
        
        #Especial case no node =>[0, 5 * 104]
        if not head:
            return head
        
        #From one node at least
        def dfs(node,hashMap):
            hashMap.append([node.val,node])
            if node.next: dfs(node.next,hashMap)
                
                
        hashMap = [] # [[val, node]]
        dfs(head,hashMap)
        
        # sorting it by val in ascending order
        sorted_hashMap = sorted(hashMap, key=lambda x: x[0])
        

        for i in range(len(hashMap)-1):
            sorted_hashMap[i][1].next = sorted_hashMap[i+1][1]   
        sorted_hashMap[-1][1].next = None
    
        return sorted_hashMap[0][1]
        
        
        
        
        
        
        
        
        