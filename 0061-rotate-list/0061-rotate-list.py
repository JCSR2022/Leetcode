# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. dfs create the list with nodes
        # 2. make nodes[-1].next point to nodes[0]
        # 3. make nodes[-k-1].next = None 
        # 4. Return as new head node[k]
        
        
        if not head:
            return head

        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
   

        nodes[-1].next = nodes[0]
    
        rotated_list_nodes = nodes[-(k % len(nodes)):] + nodes[:-k % len(nodes)]
        
        rotated_list_nodes[-1].next = None
        
        # for n in rotated_list_nodes:
        #     print(f"node:{n.val} => {n.next.val if n.next else None }  ")
        
        return rotated_list_nodes[0]
        
        
        

        
        
            
            
            
        