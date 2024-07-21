import queue

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
          
        
        #graph, topological sort // Kahn’s Algorithm
        #https://www.youtube.com/watch?v=LDNMlgBi5vg
        
        
        #steps: 
        # 1. first create Adjacency_List for rowConditions and colConditions
        # 2. find topolical order for rowConditions and colConditions
        #   2.1 using Kahns algo> find nodes without dependencies , eliminate repit
        
        
        def create_Adjacency_List(conditions):
            Adjacency_List = {n:[] for n in range(1,k+1) }
            for cond1,cond2 in conditions:
                if cond1 in Adjacency_List:
                    Adjacency_List[cond1].append(cond2)
                # else:
                #     Adjacency_List[cond1] = [cond2]
                    
            return Adjacency_List
        
        
        
        
        
        def Kahn_topological_sort(Adjacency_List):
            
            # Find degree of dependencies for each node on Adjacency_List
            degree_dependencies ={}
            for node,neighbors in Adjacency_List.items():
                if node not in degree_dependencies: 
                    degree_dependencies[node] = 0
                for neig in neighbors:
                    if neig in degree_dependencies:
                        degree_dependencies[neig] += 1
                    else:
                        degree_dependencies[neig] = 1
                
            # Find initial nodes without any dependencies
            initial_degree_0 = [ k for k,v in degree_dependencies.items() if v == 0 ]
            
            
            q = queue.Queue()
            for node in initial_degree_0:
                q.put(node)
            
            topological = []
            while not q.empty():
                node = q.get()
                topological.append(node)
  
                
                # removed from the graph nodes without dependencies (and their outgoing edges)
                if node in Adjacency_List:
                    for neighbor in Adjacency_List[node]:
                        degree_dependencies[neighbor] -= 1
                        if degree_dependencies[neighbor] == 0:
                            q.put(neighbor)
            
            # return  topological only if not internal cycles
            return topological if len(topological) == len(degree_dependencies)  else []
                    
        
        
        row_Adjacency_List = create_Adjacency_List(rowConditions)
        col_Adjacency_List = create_Adjacency_List(colConditions)
        #print(row_Adjacency_List)
        #print(col_Adjacency_List)
        
        
        topological_row = Kahn_topological_sort(row_Adjacency_List)
        topological_col = Kahn_topological_sort(col_Adjacency_List)
        #print(topological_row)
        #print(topological_col)
    
    
        if len(topological_row) == 0 or len(topological_col) == 0:
            return []
        
        
        ans = [[0]*k for _ in range(k)]
        coordinates = {n:[0,0] for n in range(1,k+1)}
        for i,n in enumerate(topological_row):
            coordinates[n][0] = i
        for j,n in enumerate(topological_col):
            coordinates[n][1] = j
        #print(coordinates)
        
        for n,coord in coordinates.items():
            ans[coord[0]][coord[1]] = n
            
        return ans
                