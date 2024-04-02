"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#from typing import Optional
class Solution:
#    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    def cloneGraph(self, node):
    
    
     #   if isinstance (node,list) and len(node) == 0:
     #       return node
        
#         if not node:
#             if not node.neighbors:
#                 error = Node(node.val)
#                 return error
#             error = Node(node.val)
#             return error
        
#         if not node.neighbors:
#             error = Node(node.val)
#             return error
          

        
# Aproach 2:
# 1. create visited hashmaps with original nodes to their corresponding copies. 
# 2. During the DFS traversal of the original graph, 
#    a copy of each node is created and added to the visited dictionary. 
# 3. neighbors of each original node are traversed.


        visited = {}
    
        def dfs(org_node):
   
            if org_node in visited:
                return visited[org_node]
        
            visited[org_node] = Node(org_node.val)
                
            for neighbors in org_node.neighbors:
                copy_neighbor = dfs(neighbors)
                visited[org_node].neighbors.append(copy_neighbor)
            
            return visited[org_node]
        
     
        return dfs(node) if node else None
                
  