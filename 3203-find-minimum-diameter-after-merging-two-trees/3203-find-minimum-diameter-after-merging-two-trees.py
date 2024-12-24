class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        #aproach:
        #BFS make a matrix dist_betwen nodes for each Tree select the node "column" with min dist between nodes
        
        
#         def build_adj_list(edges):
#             adj_list = defaultdict(list)
#             for a,b in edges:
#                 adj_list[a].append(b)
#                 adj_list[b].append(a) 
            
#             return adj_list
            
            
            
            
#         def dist_matrix(adj_list):
#             """
#             Calcula la matriz de distancias más 
#             cortas entre los nodos de un grafo no ponderado.

#             Parámetros:
#                 adj_list (dict): Lista de adyacencia 
#                                  donde las claves son nodos y los valores
#                                  son listas de nodos adyacentes.

#             Retorna:
#                 list: Matriz de distancias.
#             """
#             n = len(adj_list)
#             matrix = [[0] * n for _ in range(n)]

#             for node in adj_list.keys():
#                 q = deque([(node, 0)])  # Inicializamos la cola 
#                 visited = set()        # Conjunto para rastrear nodos visitados

#                 while q:
#                     act_node, dist = q.popleft()
#                     if act_node in visited:
#                         continue  # Si ya fue visitado, lo ignoramos

#                     visited.add(act_node)
#                     matrix[node][act_node] = dist

#                     for next_node in adj_list[act_node]:
#                         if next_node not in visited:
#                             q.append((next_node, dist + 1))

#             return matrix
        
#         def find_min_dist(adj_matrix):
#             if adj_matrix:
#                 min_val = float("inf")
#                 for row in  adj_matrix:
#                     min_val = min(max(row),min_val)
#                 return min_val
#             else:
#                 return 0
            

#         adj_list_1   = build_adj_list(edges1)
#         adj_matrix_1 = dist_matrix(adj_list_1)
#         min_val_1 = find_min_dist(adj_matrix_1)
        
#         print(adj_list_1)
#         print()
#         for i,row in enumerate(adj_matrix_1):
#             print(row,i,max(row))
#         print()
#         print(min_val_1)
#         print()
        
#         adj_list_2   = build_adj_list(edges2)
#         adj_matrix_2 = dist_matrix(adj_list_2)
#         min_val_2 = find_min_dist(adj_matrix_2)

#         print(adj_list_2)
#         print()
#         for row in adj_matrix_2:
#             print(row,max(row))
#         print()
#         print(min_val_2)
#         print()
        
#         return min_val_1 + min_val_2 + 1



        def build_graph(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def find_tree_info(edges):
            graph = build_graph(edges)
            
            def dfs(node, parent):
                height, diameter = 0, 0
                max_height1, max_height2 = 0, 0
                for child in graph[node]:
                    if child != parent:
                        child_height, child_diameter = dfs(child, node)
                        diameter = max(diameter, child_diameter)
                        if child_height + 1 > max_height1:
                            max_height2 = max_height1
                            max_height1 = child_height + 1
                        elif child_height + 1 > max_height2:
                            max_height2 = child_height + 1
                
                diameter = max(diameter, max_height1 + max_height2)
                return max_height1, diameter

            _, diameter = dfs(0, -1)
            return diameter, min(len(graph) - 1, (diameter + 1) // 2)

        diameter1, height1 = find_tree_info(edges1)
        diameter2, height2 = find_tree_info(edges2)

        return max(diameter1, diameter2, height1 + height2 + 1)
        
        
        
        