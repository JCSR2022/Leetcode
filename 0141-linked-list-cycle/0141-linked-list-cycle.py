# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Brute force soluton
        
        list_nodes = []
        lisit_nodes_val =[]
        
        def dfs(node):
            if node:
                if node in list_nodes:
                    return True
                else:
                    lisit_nodes_val.append(node.val)
                    list_nodes.append(node)
                    return dfs(node.next)
            else:
                return False
            
                    
        return dfs(head)
        