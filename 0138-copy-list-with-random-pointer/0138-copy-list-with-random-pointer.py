"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        #Especial case:
        if not head:
            return head
        
        
        # Sol (Two passes)  O(n) going trhu the linkedlist at least twice
        
        hashCopyNodes = {}
        
        current = head
        while current:
            newNode = Node(current.val)
            hashCopyNodes[current] = newNode
            current = current.next
            
        current = head
        while current:
            copy = hashCopyNodes[current]
            copy.next = hashCopyNodes[current.next] if current.next else None
            copy.random =  hashCopyNodes[current.random] if current.random else None
            current = current.next
            
        current = head
        return hashCopyNodes[current]
    
        
     
                
                
            
        