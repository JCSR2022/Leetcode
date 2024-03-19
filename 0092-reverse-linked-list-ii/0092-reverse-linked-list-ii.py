# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # aproach 
        
        dummy = ListNode(0,head)
        
        # step 1
        # reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left-1):
            leftPrev, cur = cur, cur.next
        # cur= left and leftPrev is node before left
        
        #step 2
        # reversion from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext
        
        # step 3
        # Update pointers
        leftPrev.next.next = cur
        leftPrev.next = prev
        
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # aproach
        # 1. create linked list to introduce 
        # 2. find left Node to introducea and right+1 Node
        # 3. change next on on left node and use right+1 as next to rigth node
        
        
        
#         # Crear nodos para insertar
#         nodes_to_insert = []
#         for i in range(right - left + 1):
#             nodes_to_insert.append(ListNode())
            
            
#         # Encontrar el nodo izquierdo y el nodo derecho+1
#         node = head
#         prev_node = None
#         for _ in range(left - 1):
#             prev_node = node
#             node = node.next
#         right_plus_1 = node.next
        
        
#         # Crear nodos enlazados
#         for i in range(len(nodes_to_insert) - 1):
#             nodes_to_insert[i].next = nodes_to_insert[i + 1]
        
        
#         # Conectar nodos
#         if prev_node:
#             prev_node.next = nodes_to_insert[0]
#         else:
#             head = nodes_to_insert[0]
#         nodes_to_insert[-1].next = right_plus_1
        
        
#         # Invertir los valores
#         node = nodes_to_insert[-1]
#         while node:
#             node.val = node.val if right - left == 0 else node.val + right - left
#             node = node.next
        
        
        
#         return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nodes = []
#         #create nodes:
#         for i in range(right,left-1,-1):
#             nodes.append(ListNode(i))
        
#         #link nodes
#         for i in range(len(nodes)-1):
#             nodes[i].next = nodes[i+1]
            
        
#         print([(i,i.val) for i in nodes])
        
#         #insert nodes:
#         node = head
#         while node:
#             print(f"inic val:{node.val}, inic next: {node.next.val if node.next else None}", end =",")
#             #save next node
#             if node.next: nextNode = node.next
            
#             print(f"nextNode:{nextNode.val}", end =",")
            
#             #insert head of new chain 
#             if node.val == left:
#                 node = nodes[0]
            
#             #change tail of new chain 
#             if node.val == right:
#                 nodes[-1].next = node.next
#                 break
            
#             print(f"final val:{node.val}, final next: {node.next.val if node.next else None}")
            
#             if nextNode:
#                 node = nextNode
            
            
        
     
                
            
            
                
                
            
            
                
            
        
        
        
        