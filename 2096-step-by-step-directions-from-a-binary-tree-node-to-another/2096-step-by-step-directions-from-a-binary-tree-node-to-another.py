# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
         
        #https://www.youtube.com/watch?v=JegJNGcwtFg
        
        def dfs(node,path,target):
            if not node:
                return "" #False
            
            if node.val == target:
                return path
            
            path.append("L")
            res = dfs(node.left,path,target)
            if res: return res
            
            
            path.pop()
            path.append("R")
            res = dfs(node.right,path,target)
            if res: return res
            
            path.pop()
            return  ""
            
        start_path = dfs(root,[],startValue)
        dest_path = dfs(root,[], destValue)
        
        i = 0
        while i < min(len(start_path),len(dest_path)):
            if start_path[i] != dest_path[i]:
                break
            i += 1
            
        return  "".join( ["U"] * len(start_path[i:]) + dest_path[i:])
        
            
            
        
            
            
            
            
            
            
            
            
# @#%@#%#%#@$%#$%@#$%#@$%#@%$#%@#$%#@$%@#$%$#@%#@$#$@$#%^@#$^#$@#@$%
#         # 1. use DFS till find star and dest val, buld adjacecy list on the proceses
#         # 2 use Shortest Path Algorithm to find path
        
#         Adjacency_List = {}
#         founds = 0
#         def dfs(node,prev_node=None):
#             nonlocal founds
         
#             if founds == 2:
#                 return
            
#             if node.val == startValue or node.val == destValue:
#                 founds += 1
            
#             Adjacency_List[node.val] = []
#             if prev_node: Adjacency_List[node.val].append([prev_node.val,'U'])
#             if node.left: Adjacency_List[node.val].append([node.left.val,'L'])
#             if node.right: Adjacency_List[node.val].append([node.right.val,'R'])
                
#             if node.left: dfs(node.left,node)
#             if node.right: dfs(node.right,node)
                               
                    
#         def bfs(Adjacency_List):
        
#             q = queue.Queue()
#             visited = [] 
            
#             q.put(startValue)
            
#             while not q.empty():
                
#                 node = q.get() 
#                 visited.append(node)
#                 if node == destValue:
#                     return visited
#                 if node in Adjacency_List:
#                     for neig_node,neig_move in Adjacency_List[node]:
#                         if neig_node not in visited:
#                              q.put(neig_node)
                                                
                    
                    
                    
                    
#         dfs(root)
#         print(Adjacency_List)
#         visited = bfs(Adjacency_List)
#         print(visited)
                         
#         ans = ""                
#         for i in range(len(visited)-1):
#             for node,rote in Adjacency_List[visited[i]]:
#                 if node == visited[i+1]:
#                     ans += rote
        
#         return ans
        
        
        
        
        
        