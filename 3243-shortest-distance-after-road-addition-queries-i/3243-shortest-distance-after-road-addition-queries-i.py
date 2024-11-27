from collections import deque


class Solution:

    def updateDistances(self, graph, current, distances):
        newDist = distances[current] + 1
        
        for neighbor in graph[current]:
            if distances[neighbor] <= newDist:
                continue
                
            distances[neighbor] = newDist
            self.updateDistances(graph, neighbor, distances)
    
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        distances = [n - 1 - i for i in range(n)]
        
        graph = [[] for _ in range(n)]
        for i in range(n-1):
            graph[i + 1].append(i)
        
        answer = []
        
        for source, target in queries:
            graph[target].append(source)
            distances[source] = min(distances[source], distances[target] + 1)
            self.updateDistances(graph, source, distances)
            
            answer.append(distances[0])
        
        return answer    
    
#--------------------------------------------------------------    
    # def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
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
        
        
#         def BFS_short_path(adjacen_list):
#             #BFS find short path form node 0 to node n-1
            
#             min_dist = float("inf")
#             city = 0
#             q = deque([(city, 0)]) 
#             visited =set( )
            
#             while q:
#                 city,dist = q.popleft() 
#                 visited.add(city)
#                 print(q,city,dist,visited,min_dist)
                
#                 if city == n-1:
#                     min_dist = min(min_dist,dist)
#                     continue
                
#                 for next_city in adjacen_list[city]:
#                     if next_city not in visited:
#                         q.append((next_city,dist+1))
            
#             return min_dist        
        
        
#         adjacen_list = {i:[i+1]  for i in range(n-1)}
#         adjacen_list[n-1] = []
#         ans = []
#         for u,v in queries:
#             adjacen_list[u].append(v)
#             print(adjacen_list)
#             ans.append(BFS_short_path(adjacen_list))
        
        
#         return ans
        
#good
#----------------------------------------
     #Improve   

#         def short_path():
#             q = deque()
#             q.append((0,0))
#             visited = set()
            
#             while q:
#                 city,dist = q.popleft()
#                 visited.add(city)
                
#                 if city == n-1:
#                     return dist
            
#                 for next_city in adj_list[city]:
#                     if next_city not in visited:
#                         q.append((next_city,dist+1))
            

#         adj_list = [[i+1] for i in range(n)]
#         ans = []
#         for u,v in queries:
#             adj_list[u].append(v)
#             ans.append(short_path())
        
 
#         return ans

        
#--------------------------------------------------------------

#        # Function to run Dijkstra's algorithm
#         def dijkstra(start: int, end: int, graph: Dict[int, List[Tuple[int, int]]]) -> int:
#             # Min-heap for priority queue
#             heap = [(0, start)]  # (distance, node)
#             distances = [float('inf')] * n
#             distances[start] = 0
            
#             while heap:
#                 curr_dist, curr_node = heappop(heap)
                
#                 # If we reach the destination, return the distance
#                 if curr_node == end:
#                     return curr_dist
                
#                 # Skip if we find a longer distance in heap
#                 if curr_dist > distances[curr_node]:
#                     continue
                
#                 # Explore neighbors
#                 for neighbor, weight in graph[curr_node]:
#                     new_dist = curr_dist + weight
#                     if new_dist < distances[neighbor]:
#                         distances[neighbor] = new_dist
#                         heappush(heap, (new_dist, neighbor))
            
#             # If unreachable, return infinity
#             return distances[end]
        
#         # Initialize graph as adjacency list
#         graph = {i: [] for i in range(n)}
#         for i in range(n - 1):
#             graph[i].append((i + 1, 1))  # Unidirectional edge with weight 1
        
#         result = []
        
#         for u, v in queries:
#             # Add the new road
#             graph[u].append((v, 1))
            
#             # Calculate shortest path from 0 to n-1
#             shortest_path_length = dijkstra(0, n - 1, graph)
#             result.append(shortest_path_length)
        
#         return result


#--------------------------------------------------------------


#        # Dijkstra's algorithm modify:
    
#         def dijkstra() -> int:
   
#             heap = [(0,0)]  
#             distances = [float('inf')] * n
#             distances[0] = 0
#             #visited  = set()
            
#             while heap:
#                 curr_dist, curr_node = heappop(heap)
#                 #visited.add(curr_node)
                
#                 if curr_node == n-1:
#                     return curr_dist
                
#                 # Skip if we find a longer distance in heap
#                 if curr_dist > distances[curr_node]:
#                     continue
                
#                 # Explore neighbors
#                 for neighbor in graph[curr_node]:
#                     #if neighbor not in visited:
#                     new_dist = curr_dist + 1
#                     if new_dist < distances[neighbor]:
#                         distances[neighbor] = new_dist
#                         heappush(heap, (new_dist, neighbor))

                        
#         # Initialize graph as adjacency list
#         graph = [[i+1]  for i in range(n-1)]

#         result = []
#         for u, v in queries:
#             # Add the new road
#             graph[u].append(v)
#             result.append(dijkstra())
            
   
#         return result


