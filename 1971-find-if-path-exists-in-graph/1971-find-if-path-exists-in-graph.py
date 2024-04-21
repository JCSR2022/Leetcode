class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        adj_list = collections.defaultdict(list)
        
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        seen = set()
        def dfs(node):
            if node == destination:
                return True
            
            seen.add(node)
            for v in adj_list[node]:
                if v not in seen and dfs(v):
                    return True
            return False
        

        
        return dfs(source)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         vet = {} #vertex_edges_table
#         for i in range(n):
#             vet[i] = []
            
#         for u,v in edges:
#             vet[u].append(v)
#             vet[v].append(u)
    

#         def find_path(s,d):
#             print(s)
#             if d in s:
#                 return True
#             else:
#                 ans = True
#                 for vertex in s:
#                     isfound = False
#                     if vertex not in visited:
#                         visited.add(vertex)
#                         isfound = find_path(vet[vertex],d)
#                     ans = ans and isfound
                    
#                 return ans
        
#         print(vet)
#         s = vet[source]
#         visited = set() 
        
#         return find_path(s,destination)













#         def buld_graph(n,edges):
#             vet = {} #vertex_edges_table
#             for i in range(n):
#                 vet[i] = []
            
#             #bi-directional 
#             for u,v in edges:
#                 vet[u].append(v)
#                 vet[v].append(u)
            
#             return vet
        
#         graph = buld_graph(n,edges)
        
#         print(graph)
        
#         visited = set()
        
#         def graph_traverse(graph,s,d):
            
#             if d in graph[s]:
#                 return True
            
#             ans = False
#             for new_vertex in graph[s]:
#                 if new_vertex not in visited:
#                     visited.add(new_vertex)
#                     ans = graph_traverse(graph[new_vertex],s,d)
#                     if ans: break
            
#             return ans
        
        
#         graph_traverse(graph,source,destination)
        
#         return True
        