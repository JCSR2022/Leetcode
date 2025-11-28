class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
#         adj_list = {}
#         for l,r in edges:
#             if l in adj_list:
#                 adj_list[l].append(r)
#             else:
#                 adj_list[l] = [r]
            
#             if r in adj_list:
#                 adj_list[r].append(l)
#             else:
#                 adj_list[r] = [l]
        
#         print(adj_list)
#         sum_val =  values.copy()
#         count = [0]
#         visited = set()
        
#         q = deque([0])
        
#         while q:
#             node = q.popleft()
#             if node not in visited:
#                 visited.add(node)

#             for next in  
            
            
        
        
        
            
        
#         return count

#----------------------------------------------


        G = defaultdict(list)
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
        components = 1
        def dfs(v, u):
            nonlocal components
            res = values[v]
            for w in G[v]:
                if w != u:
                    cur = dfs(w, v)
                    res += cur
                    if cur%k == 0:
                        components += 1
            return res
        dfs(0, -1)
        return components
        
        