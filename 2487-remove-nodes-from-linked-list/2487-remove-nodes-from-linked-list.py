# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # aproach brute force:
        #  create
        #  [(val_0,node_0),...(val_i,node_i)]
        #  where to insert (val_i,node_i) val_i< val_i-1, ... Val_0 

        val_nodes = []
        #vals = 1 <= Node.val <= 105
        def dfs(node):
            val_nodes.append((node.val,node))
            if node.next:
                dfs(node.next)
        
        dfs(head)
        
        
        ans = [(float('-inf'),None)]
        for v,n in val_nodes:
            while ans and v > ans[-1][0]:
                ans.pop()
            ans.append((v,n))
            
        
        if len(ans) == 1:
             ans[0][1].next = None
            
        for i in range(1,len(ans)):
             ans[i-1][1].next = ans[i][1]
        ans[-1][1].next = None
        
        
        return ans[0][1]
                
                
                
            
                
                        
        
        