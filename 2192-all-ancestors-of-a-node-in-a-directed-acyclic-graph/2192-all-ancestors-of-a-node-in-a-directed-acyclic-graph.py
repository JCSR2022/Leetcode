class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        # Reverse Graph -> Finding all children of node
        for i in range(len(edges)):
            edges[i][0], edges[i][1] = edges[i][1], edges[i][0]
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1]) 
        cache = {}
        # DFS with cache (memoization DP)
        def dfs(node):
            if node in cache: return cache[node]
            children = set([node])
            for next_node in graph[node]:
                # Extend the set with all of new children
                children |= dfs(next_node) 
            cache[node] = children
            return cache[node]
        res = []
        for i in range(n):
            res_i = dfs(i).copy()
            res_i.remove(i) # remove its self as a child
            res.append(sorted(list(res_i))) # output need to be sorted
        return res
        
#         indegrees = [0]*n
#         for o,d in edges:
#             indegrees[d] +=1 
        
#         Adjacency_List = [set() for i in range(n) ]
#         for o,d in  edges:
#             Adjacency_List[o].add(d)
        
#         print(Adjacency_List)
        
#         print(indegrees)
        
        
        
        
        
        
#         return [[0]]
        
        
        
        
        
        
        
        
        
        
        
        
        #No pude $#%#$^$%^$%^$#%^$%&$
#         # Adjacency_List = {i:[] for i in range(n) }
#         # for o,d in  edges:
#         #     Adjacency_List[o].append(d)
#         # print(Adjacency_List)
        
#         ancestor_List = [set() for i in range(n) ]
#         for d,o in  edges:
#             ancestor_List[o].add(d)
        
#         print(ancestor_List)
        
        
#         def findAncest(node,ancestor_List):
            
#             if not node:
#                 return 
            
#             ans = set()
#             for anc in node:
#                 if ancestor_List[anc]:
#                     ans.add(findAncest(anc,ancestor_List))
#             return ans  
                
#         ans = findAncest(3,ancestor_List) 
        
#         print(ans)
        
#         return [[0]]