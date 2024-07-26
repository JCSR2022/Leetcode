class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        #brute force, bfs for each node as long as nodes are in distanceThreshold
        
#             def create_adjancency_List(edges):
                
#                 adjacenList = {}
#                 for fromi, toi, weighti in edges:
#                     if fromi not in adjacenList:
#                         adjacenList[fromi] = [[weighti,toi]]
#                     else:
#                         adjacenList[fromi].append([weighti,toi])

#                     if toi not in adjacenList:
#                         adjacenList[toi] = [[weighti,fromi]]
#                     else:
#                         adjacenList[toi].append([weighti,fromi])
                        
#                 return adjacenList
            
#             import queue
#             def min_distances(start,adjancency_List):
#                 nodes = [float(inf) for _ in range(len(adjancency_List)) ]
#                 nodes[start] = 0
                
#                 q = queue.Queue()
#                 q.put((0,start))
                
#                 while not q.empty():
#                     node_dist, node = q.get()
                
#                     for weighti,toi in adjancency_List[node]:
#                         nodes[toi] = min(node_dist+weighti,nodes[toi])
#                         q.put((nodes[toi],toi))
                            
#                 print(nodes)
                
            
#             adjancency_List = create_adjancency_List(edges)
#             print(adjancency_List)

#             min_distances(0,adjancency_List)


#             return 0
        
        
        
            
            
            
            
#        #nononono     00000000000000000000000000000
#             import queue
#             def BFS_Threshold(start,adjancencyList,Threshold):
                
#                 q = queue.Queue()
#                 visited = set()
#                 q.put((0,start))
                
#                 while not q.empty():
#                     dist,node = q.get()
#                     if dist <= Threshold:
#                         visited.add(node)

#                         if node in adjancencyList:
#                             for  weighti,toi in adjancencyList[node]:
#                                 if toi not in visited:
#                                     if weighti + dist <= Threshold:
#                                         q.put((dist + weighti,toi))

#                 return visited
                
            
#             neighboring_cities ={}
#             for node in adjancency_List.keys():
#                 neighboring_cities[node] = BFS_Threshold(node,adjancency_List,distanceThreshold)
#             print(neighboring_cities)
            
#             distances = [len(BFS_Threshold(i,adjancency_List,distanceThreshold)) for i in range(n)]
#             ans = [ i for i in range(len(distances)) if distances[i] == min(distances)  ]
#             print(distances,ans ,ans [-1])
#             return ans[-1]
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # firts check number of cities on distanceThreshold
        # for each city create the list of cities on distanceThreshold

        def Floyd_Warshall(edges):
            # Algoritmo de Floyd-Warshall 
            distances = [[float('inf')] * n for _ in range(n)]
            # Set the initial distances based on the given edges
            for edge in edges:
                distances[edge[0]][edge[1]] = edge[2]
                distances[edge[1]][edge[0]] = edge[2]
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
            return distances

        def func_min(lst):
            # Encuentra el índice del mínimo en la posición más grande
            list_inv = lst[::-1]
            return len(lst)-list_inv.index(min(list_inv))-1    


        distances = Floyd_Warshall(edges)

        # Para visualizar mejor las distancias y las ciudades
        Cities_neighboring = {key: [] for key in range(n)}
        for i,distances_city_i in enumerate(distances):
            for j,distance in  enumerate(distances_city_i):
                if i !=j and distance<=distanceThreshold:
                    Cities_neighboring[i].append([j,distance])
                    
        quantity_cities_in_range= [ len(cities_in_distance) for cities_in_distance in Cities_neighboring.values()]

        return func_min(quantity_cities_in_range)     

