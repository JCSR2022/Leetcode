from queue import PriorityQueue

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        
        graph ={}
        for i, original_letter in enumerate(original):
            if original_letter not in graph:
                graph[original_letter] = {}
            target_letter = changed[i]
            graph[original_letter][target_letter] = min(cost[i], graph[original_letter].get(target_letter, float("inf")))
            
            
        total = 0 
        memo = {}
        
        for i in range(len(source)):
            if source[i] != target[i]:
                result = self.find_path(source[i],target[i],graph,memo)
                if result == -1:
                    return -1
                total += result
        return total 

    
    def find_path(self,source,target, graph,memo):
        if (source,target) in memo:
            return memo[(source,target)]
        
        pq = PriorityQueue()
        pq.put((0,source))
        seen = set()
        
        while not pq.empty():
            cost,letter = pq.get()
            if letter == target:
                memo[(source,target)] = cost
                return cost
            if letter not in seen:
                seen.add(letter)
                neighbors = graph.get(letter,[])
                for neig in neighbors:
                    pq.put((cost + neighbors[neig],neig ))
        return -1
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #%#%@#%@%@%@ Time Limit Exceeded $^#@^@^#$%&%^&%*^@#!@
        
        
#         #build a adjacency_list nodes from original to change with the value of cost as edge
#         # (dijkstra`s) find the min path from letter in source to target and reomve nodes implicated on change
#         #safe as hashmap , add all change//
        
#         def make_Adjacency_List():
#             size = len(original)
#             Adjacency_List = {node:[] for node in set(original+changed)}
#             for i in range(size):
#                 Adjacency_List[original[i]].append((cost[i],changed[i]))
#             return Adjacency_List
                    
        
#         import queue
#         def dijkstra(Adjacency_List,start):
            
#             visited = { k : False  for k in Adjacency_List.keys()}
#             dist = {k:float(inf) for k in Adjacency_List.keys()}   
#             dist[start] = 0
        
#             q = queue.PriorityQueue()
#             q.put((dist[start],start))
            
#             while not q.empty():
#                 distance, node = q.get()
                
#                 if visited[node]:continue
#                 visited[node] = True
                
#                 for edge_dist, neigh_node in Adjacency_List[node]:
#                     if visited[neigh_node]:continue
#                     new_distance = distance + edge_dist
#                     if new_distance < dist[neigh_node]:
#                         dist[neigh_node] = new_distance
#                         q.put((new_distance,neigh_node))
                
#             return {k:v for k,v in dist.items()  if v < float('inf') and k != start  }
        
        
    
#         Adjacency_List = make_Adjacency_List()
#         #print(Adjacency_List)
        
#         hash_map = {}
#         for o in original:
#             hash_map[o] = dijkstra(Adjacency_List,o)
#         #print(hash_map)
         
#         ans = 0
#         for i in range(len(source)):
#             if source[i] != target[i]:
#                # print(i,source[i],target[i],  hash_map[source[i]][target[i]])
#                 if source[i] not in hash_map or target[i] not in hash_map[source[i]]:
#                     return -1
#                 else:
#                     ans += hash_map[source[i]][target[i]]
#         return ans
        
        
        
        