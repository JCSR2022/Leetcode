import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
     
    
        #1.make adajance lis with prereq
        #make Topological using kal`s Algorithm
        
        def create_Adjacency_List(prerequisites):
            Adjacency_List ={}
            for req,cu in prerequisites:
                if cu in Adjacency_List:
                    Adjacency_List[cu].add(req)
                else:
                    Adjacency_List[cu] = {req}
            return Adjacency_List
             
        def KalAlg(Adjacency_List):
            
            incoming_degree = defaultdict(int) 
            for node,neighbors in Adjacency_List.items():
                incoming_degree[node] += 0
                for n in neighbors:
                    incoming_degree[n] +=1
            #print("incoming_degree:",incoming_degree)
            
            
            nodes_degree_0 = [node for node,degree in incoming_degree.items() if degree == 0  ]

            q = queue.Queue()
            for node_degree_0 in nodes_degree_0:
                q.put(node_degree_0)
            
            
            Topological_Order = []
            while not q.empty():
                node = q.get()
                Topological_Order.append(node)
                
                for neigh in Adjacency_List[node]:
                    incoming_degree[neigh] -=1
                    if incoming_degree[neigh] == 0:
                        q.put(neigh)
                        
            return Topological_Order
                
        
        Adjacency_List = create_Adjacency_List(prerequisites)
        for node in [n for n in range(numCourses)]:
            if node not in Adjacency_List:
                Adjacency_List[node] = []
                 
        Topological_Order = KalAlg(Adjacency_List)
            
        if len(Topological_Order) == numCourses:
            return Topological_Order
        else:
            return []
 
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#         #1.make adajance lis with prereq
#         #make Topological Sort Algorithm
        
#         def create_Adjacency_List(prerequisites):
#             Adjacency_List ={}
#             for req,cu in prerequisites:
#                 if cu in Adjacency_List:
#                     Adjacency_List[cu].add(req)
#                 else:
#                     Adjacency_List[cu] = {req}
#             return Adjacency_List
             
#         def dfs(Adjacency_List,curses,node,visited):
#             if node not in visited:
#                 if node in Adjacency_List:
#                     for nextNode in Adjacency_List[node]:
#                         dfs(Adjacency_List,curses,nextNode,visited)
#                 visited.append(node)
#                 if node in curses:
#                     curses.remove(node)
            
#         curses = set([n for n in range(numCourses)])
#         print(curses)
        
#         Adjacency_List = create_Adjacency_List(prerequisites)
#         print(Adjacency_List)
        
#         v = []
#         while curses:
#             #print(v,curses)
#             dfs(Adjacency_List,curses,curses.pop(),v)
            
            
#         return v[::-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
#        def bfs(star,Adjacency_List):
#             q = queue.Queue()    
#             visited = []

#             q.put(star)
#             visited.append(node)
            
#             while not q.empty():
#                 node = q.get()               
                
#                 if node in Adjacency_List:
#                     for next_node in Adjacency_List[node]:
#                         if next_node not in visited:
#                             visited.append(node)
#                             q.put(next_node)
                
#             return visited    
    
    
    
    
    
    
    
    
#         pre_r = {}
#         req_p = {}
#         for cur in range(numCourses):
#             pre_r[cur] = []
#             req_p[cur] = []
        
#         for pre,cur in prerequisites:
#             pre_r[pre].append(cur)
#             req_p[cur].append(pre)
            

        
#         print(pre_r)
#         print(req_p)
        
#         return [0]