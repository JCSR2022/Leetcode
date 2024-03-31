"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        
        # aproach dfs( pre order traversal),
        #  save level and nodes of level in a hash
        #  then use the ahsh to indicate the nexts nodes..
        
        
        hashNodes = {}
        def dfsPreOrderTra(node,hashNodes,level = 0):
            if node:
                if level in hashNodes:
                    hashNodes[level].append(node) 
                else:
                    hashNodes[level] = [node]
                
                dfsPreOrderTra(node.left,hashNodes,level+1)  
                dfsPreOrderTra(node.right,hashNodes,level+1)          
            
        dfsPreOrderTra(root,hashNodes)
        
        # for level,nodes in hashNodes.items():
        #     values = [node.val for node in nodes]
        #     print(level,values)
        
        for level,nodes in hashNodes.items():
            if len(nodes) > 1:
                for i in range(len(nodes)-1):
                    nodes[i].next = nodes[i+1]
                    
        return root
                
        
        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        