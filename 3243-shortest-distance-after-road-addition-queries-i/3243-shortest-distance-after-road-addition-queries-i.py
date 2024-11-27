from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        #brute force:
        # make arr distances, with min distance to reach each city
        # For each query modify distances , dist[vi] = min(dist[vi],dist[ui]+1)
        # for j in range vi -> n-1  dist[j] = min(dist[j],dist[ui]+1)
        #return dist[-1]
        
        
#         dist = list(range(n))
#         ans = []
#         for u,v in queries:
#             if dist[u]+1 < dist[v]:
#                 dist[v] = dist[u]+1
#                 for j in range(v+1,n):
#                     if dist[j-1] + 1 < dist[j]:
#                         dist[j] = dist[j-1] + 1
#                     else:
#                         break
#             print((u,v),dist)
#             ans.append(dist[-1])
            
#         return ans

# NOOOOO
#-------------------------------------------------------------------------

        #next_city = list(range(1,n-1))
        
#         next_city = [2,2,3,4,5,6,7]
        
#         i = 0
#         cont = 0
#         while i<7:
#             cont += 1
#             i = next_city[i]
        
#         print(cont)
        
        
        
        
#         ans =[]
#         return ans
#nooooo    
#-----------------------------------------------------   

# make adjance list, actualize with queries and for each find short path 
        
        
        def BFS_short_path(adjacen_list):
            #BFS find short path form node 0 to node n-1
            
            min_dist = float("inf")
            city = 0
            q = deque([(city, 0)]) 
            visited =set( )
            
            while q:
                city,dist = q.popleft() 
                visited.add(city)
                #print(q,city,dist,visited,min_dist)
                
                
                if city == n-1:
                    min_dist = min(min_dist,dist)
                    continue
                
                for next_city in adjacen_list[city]:
                    if next_city not in visited:
                        q.append((next_city,dist+1))
            
            return min_dist        
        
        
        adjacen_list = {i:[i+1]  for i in range(n-1)}
        adjacen_list[n-1] = []
        ans = []
        for u,v in queries:
            adjacen_list[u].append(v)
            #print(adjacen_list)
            ans.append(BFS_short_path(adjacen_list))
        
        
        return ans
        
        
        
        
        
        
        
        




