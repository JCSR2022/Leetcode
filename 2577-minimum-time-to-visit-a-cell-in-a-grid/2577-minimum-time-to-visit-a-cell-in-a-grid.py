import queue

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        
#         m = len(grid)
#         n = len(grid[0])
        
#         if grid[0][1] > 1 or grid[1][0] > 1:
#             return -1
        
        
#         def posibleMoves(i,j):
#             moves = []
#             #up:
#             if i > 0: moves.append([i-1,j])
#             #down:
#             if i < m : moves.append([i+1,j])
#             #left:
#             if j > 0 : moves.append([i,j-1])
#             #right
#             if j < m : moves.append([i,j+1])
#             return moves
        
        
#         def bfs_inverse():
        
#             heap = [] 
#             heapq.heappush(heap,(grid[-1][-1],m-1,n-1)        
#             times = [grid[-1][-1]]
#             visited = set()
                           
#             while heap:
#                 time,i,j = heappop(heap)
#                 visited.add((i,j))
                           
#                 if i == 0 and j == 0:
#                     return times
                           
#                 for n_i,n_j in posibleMoves(i,j):
#                     if (n_i,n_j) not in visited:
#                         heapq.heappush(heap,(grid[n_i][n_j],n_i,n_j))  
                           
#-----------------------------------------------------------------           
    
#convert grid in weighted graph, use dijstra`s to find path, return max of that path
        
#         m = len(grid)
#         n = len(grid[0])       
        
        
#         if grid[0][1] > 1 and grid[1][0] > 1:
#             return -1
        
#         def posibleMoves(i,j):
#             moves = []
#             #up:
#             if i > 0: moves.append((i-1,j))
#             #down:
#             if i < m-1 : moves.append((i+1,j))
#             #left:
#             if j > 0 : moves.append((i,j-1))
#             #right
#             if j < n-1 : moves.append((i,j+1))
#             return moves     
        
        
#         def Eager_Dijkstra(adjancency_List):
            
#             inic_vert = (0,0)
#             final_vert = (m-1,n-1)
#             q= queue.PriorityQueue()
#             visited = []
#             shortDist ={node:float('inf') for node in  adjancency_List.keys() }
#             previos = {node:None for node in  adjancency_List.keys() }
#             shortDist[inic_vert] = 0

#             q.put((0,inic_vert))

#             while not q.empty():
#                 edge_val,node =  q.get() 
#                 visited.append(node)

#                 for neigh_edge_val,neigh in adjancency_List[node]:
#                     if neigh not in visited:
#                         q.put((neigh_edge_val, neigh))

#                     if  shortDist[node] + neigh_edge_val < shortDist[neigh] :
#                         shortDist[neigh] = shortDist[node]+ neigh_edge_val
#                         previos[neigh] = node

#                     if final_vert in visited:
#                         return shortDist, previos

#             return shortDist, previos  

        
#         def ans_format(shortDist, previos):
#             inic_vert = (0,0)
#             final_vert = (m-1,n-1)
#             max_dist = shortDist[final_vert]
#             path = []
#             vert = final_vert
#             while vert:
#                 path.append(vert)
#                 vert = previos[vert]
#             return [ grid[i][j] for i,j in path[::-1]]
        
        
        
#         My_Adjacency_List = {}
#         for i in range(m):
#             for j in range(n):
#                 My_Adjacency_List[(i,j)] = [(grid[x][y],(x,y)) for x,y  in posibleMoves(i,j)]
        

#         shortDist, previos = Eager_Dijkstra(My_Adjacency_List)   
#         times = ans_format(shortDist, previos)

#         print(times[1:])
        
#         cont_t = 0
#         for t in times[1:]:
#             if t > cont_t + 1:
#                 cont_t = cont_t + (t - cont_t-1)*2+1
#             else:
#                 cont_t += 1 
#             print(t,cont_t)

#         return cont_t

#------------------------------------------------------------

#https://www.youtube.com/watch?v=Kj98r8IgJOQ

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        
        def posibleMoves(i,j):
            moves = []
            #up:
            if i > 0: moves.append((i-1,j))
            #down:
            if i < rows-1 : moves.append((i+1,j))
            #left:
            if j > 0 : moves.append((i,j-1))
            #right
            if j < columns-1 : moves.append((i,j+1))
            return moves 
        
        
        rows = len(grid)
        columns = len(grid[0])       
        visited = set()
        min_heap = []
        heapq.heappush(min_heap,(0,0,0)) #time,r,c 
        visited.add((0,0))
        
        while min_heap:
            t,r,c =  heappop(min_heap)
            
            
            if (r,c) == (rows-1,columns-1):
                return t
            
            neighbors = posibleMoves(r,c)
            
            for nr,nc in neighbors:
                if (nr,nc) not in visited: 
                    visited.add((nr,nc))
                    add_wait  = 0 
                    if abs(grid[nr][nc] - t) % 2 == 0:
                        add_wait  = 1
                    nt = max(grid[nr][nc] + add_wait, t+1)  

                    heapq.heappush(min_heap,(nt,nr,nc))
        
        
            
            
            