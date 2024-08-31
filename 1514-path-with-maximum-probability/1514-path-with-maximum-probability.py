import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        #make  Adjacency_List
        Adjacency_List = collections.defaultdict(list)
        for (edg_or,edg_dest),prob in zip(edges,succProb):
            Adjacency_List[edg_or].append((prob,edg_dest))
            Adjacency_List[edg_dest].append((prob,edg_or))
        
        #print(Adjacency_List)
        
        
        #improve usig the fact that p1*p2 is always < p1 or  p2!!!!!
        def dijkstra(Adjacency_List,start,end):
            visited = set()
  
            heap = [(-1,start)]
            heapq.heapify(heap)
            
            while heap:
                prob,node = heapq.heappop(heap)
                visited.add(node)
                
                if node == end:
                    return -prob
                
                for neig_prob,neig_node in Adjacency_List[node]:
                    if neig_node not in visited:
                        heapq.heappush(heap, (neig_prob*prob ,neig_node))
                    
            
            return 0
        
        return dijkstra(Adjacency_List,start_node,end_node)
        
        
 



#         #make  Adjacency_List
#         Adjacency_List = collections.defaultdict(list)
#         for (edg_or,edg_dest),prob in zip(edges,succProb):
#             Adjacency_List[edg_or].append((prob,edg_dest))
#             Adjacency_List[edg_dest].append((prob,edg_or))
        
#         #print(Adjacency_List)
        
#         def dijkstra(Adjacency_List,start,end):
#             visited = set()
#             proba = [0]*n
#             proba[start] = 1
            
#             heap = [(-1,start)]
#             heapq.heapify(heap)
            
#             while heap:
#                 prob,node = heapq.heappop(heap)
                
#                 prob = -prob
#                 if node in visited: continue
#                 visited.add(node)
                
#                 if node == end:
#                     return prob
                
#                 #print(visited,heap,proba,prob,node)
                
#                 for neig_prob,neig_node in Adjacency_List[node]:
#                     #print("neig_prob,neig_node:",neig_prob,neig_node)
#                     new_prob = neig_prob*prob 
                    
#                     if new_prob > proba[neig_node]:
#                         proba[neig_node] = new_prob
#                         heapq.heappush(heap, (-new_prob,neig_node))
                    
            
#             return proba[end_node]
        
#         return dijkstra(Adjacency_List,start_node,end_node)
        

        
        
        
        
        
 
#         #make  Adjacency_List
#         Adjacency_List = {x:[] for x in range(n)}
#         for  (org,end),prob in zip(edges,succProb):
#             Adjacency_List[org].append( (prob,end))
#             Adjacency_List[end].append( (prob,org))
        
#         #print(Adjacency_List)
        
        
        
#         proba = [ 0 ] * n
#         prev_node = [-1] * n 
#         import heapq
#         def Dijkstras(Adjacency_List,start):
#             proba[start] = 1
#             visited = []
            
            
#             heap = [(-1,start)]
#             heapq.heapify(heap)
            
            
#             while heap:
#                 pro,node =  heapq.heappop(heap)
                
#                 pro = -1*pro
#                 if node in visited: continue
#                 visited.append(node)
                
                
#                 for (new_pro,adj_node) in Adjacency_List[node]:
                    
#                     total_pro = new_pro * pro
#                     if total_pro > proba[adj_node]:
#                         proba[adj_node] = total_pro
#                         prev_node[adj_node] = node
                    
#                         heapq.heappush(heap,(-1*total_pro,adj_node))
                    
                
#         Dijkstras(Adjacency_List,start_node)
#        # print(proba)
#        # print(prev_node) 
        
        
        
#         return proba[end_node]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # 0. make Adjacency_List
#         # 1. check there is  path from start to end (can be make on Dijkstra’s)
#         # 2. Dijkstra’s Shortest Path Algorithm 
        
                
#         def make_Adjacency_List(n,edges,succProb):
#             Adjacency_List = {x:[] for x in range(n)}
            
#             for (edg0,edg1),prob in zip(edges,succProb):
# #                 if  edg0 not in Adjacency_List  or edg1 not in Adjacency_List:
# #                     return "Edges no valid"
#                 Adjacency_List[edg0].append((prob,edg1)) 
#                 Adjacency_List[edg1].append((prob,edg0))
        
#             return Adjacency_List
        
        
# #        import queue
# #         def Dijkstras(Adjacency_List,start):
# #             # Init..
# #             visited = [False for _ in Adjacency_List]
# #             probability = [ 0  for _ in Adjacency_List]
# #             probability[start] = 1

            
# #             q = queue.Queue()
# #             q.put((1, start))
    
# #             while not q.empty():
# #                 prob,index = q.get()
# #                 #print((prob,index),probability, end=", ")
                
# #                 if visited[index]: continue
# #                 visited[index] = True
# #                 #print("vis:",visited,end=", ")
                
                
# #                 for n_prob, n_index in Adjacency_List[index]:
# #                     #if visited[n_index]:continue
                        
# #                     new_prob = prob * n_prob
# #                     #print("new:,", prob,(n_prob, n_index),new_prob )
                    
# #                     if new_prob > probability[n_index]:
# #                         probability[n_index] = new_prob
# #                         q.put((new_prob, n_index))
              
# #             return probability

#         def Dijkstras(Adjacency_List, start):
#             # Initialize
#             max_prob = [0.0] * len(Adjacency_List)
#             max_prob[start] = 1.0
#             max_heap = [(-1.0, start)]  # Using a max-heap, store (-probability, node)

#             while max_heap:
#                 prob, node = heapq.heappop(max_heap)
#                 prob = -prob  # Convert back to positive

#                 # Iterate over neighbors
#                 for next_prob, neighbor in Adjacency_List[node]:
#                     new_prob = prob * next_prob

#                     if new_prob > max_prob[neighbor]:
#                         max_prob[neighbor] = new_prob
#                         heapq.heappush(max_heap, (-new_prob, neighbor))

#             return max_prob


#         Adjacency_List = make_Adjacency_List(n,edges,succProb)
#         #print(Adjacency_List)
        
#         probability = Dijkstras(Adjacency_List,start_node)
#         #print(probability)
        
#         return probability[end_node]