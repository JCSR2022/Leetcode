class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    




















#-------------------------------------------------

        n = len(colors)
        
        #make adj list
        adj_list = {i: [] for i in range(n)}  
        for aj, bj in edges:
            adj_list[aj].append(bj)

        #   first check cycles -----------------------
        curr_search = set()
        visited = set()
        def dfsIsCycle(node):
            if node in curr_search:
                return True

            if node in visited:
                return False

            curr_search.add(node)
            visited.add(node)

            for neigh in adj_list[node]:
                if dfsIsCycle(neigh):
                    return True

            curr_search.remove(node)
            return False

        print(dict(adj_list))

        for node in adj_list:
            if node not in visited:
                if dfsIsCycle(node):
                    return -1
        #       ------------------------------------    

        visited = set()
        mem_color_nodes = {}
        def dfsFindColors(node):
            if node in mem_color_nodes:
                return  mem_color_nodes[node]

            visited.add(node)

            curr_colors = defaultdict(int)
            for neig in adj_list[node]:
                for color,cnt in dfsFindColors(neig).items():
                    curr_colors[color] = max(curr_colors[color],cnt)

            curr_colors[colors[node]] +=1
            mem_color_nodes[node] = curr_colors 
            return mem_color_nodes[node]

        ans = 0
        for node in adj_list:
            if node not in visited:
                node_colors =  dfsFindColors(node)
                ans = max(ans, max(node_colors.values()))
    
        return ans

#------------------------------------------------
# #eres una mierda que no sirve para nada



                















#-------------------------------------------------------
#         #special condition:
#         if len(edges) == 0 and len(colors) > 0:
#             return 1


   

#         adj_list = {}
#         for aj, bj in edges:
#             if aj in adj_list: 
#                 adj_list[aj].append(bj)
#             else:
#                 adj_list[aj] = [bj]

#             if bj not in adj_list:  
#                 adj_list[bj] = []
        
#         #print(adj_list)

#         #first check if cycle------------------------
#         # visited = set()
#         # def dfs(node):
#         #     print(visited,node,node in visited )
#         #     if node in visited and len(adj_list[node]) != 0:
#         #         return -1
#         #     visited.add(node)
        
#         #     for neighbor in adj_list[node]:
#         #         if dfs(neighbor) ==-1:
#         #             return -1
#         #     return 0

#         # nodes = list(adj_list.keys()) 
#         # while nodes:
#         #     node = nodes[0]
#         #     if dfs(node) == -1:
#         #         return -1
#         #     nodes = [n for n in nodes if n not in visited]


#         def has_cycle(adj_list):
#             visited = set()
#             rec_stack = set()  # tracks nodes in the current DFS path

#             def dfs(node):
#                 if node in rec_stack:
#                     return True  # cycle detected
#                 if node in visited:
#                     return False  # already fully explored

#                 visited.add(node)
#                 rec_stack.add(node)

#                 for neighbor in adj_list[node]:
#                     if dfs(neighbor):
#                         return True

#                 rec_stack.remove(node)
#                 return False

#             for node in adj_list:
#                 if node not in visited:
#                     if dfs(node):
#                         return True
#             return False

#         if has_cycle(adj_list):
#             return -1

#         #-------------------------------------------------


#         #secund find max colors------------------------
#         colors_count = defaultdict()
#         visited = set()
#         def dfs2(node):
            
#             visited.add(node)

#             if node in colors_count:
#                 return colors_count[node]

#             curr_count =defaultdict(int)
#             for neighbor in adj_list[node]:
#                 neig_count = dfs2(neighbor)
#                 for color,count in neig_count.items():
#                     curr_count[color] = max(curr_count[color],count)

#             curr_count[colors[node]] += 1
#             colors_count[node] = curr_count 
#             return colors_count[node]

#         nodes = list(adj_list.keys()) 
#         ans = 0
#         while nodes:
#             node = nodes[0]
#             curr_node_colors_count =  dfs2(node) 
#             ans = max(ans,max(curr_node_colors_count.values()))
#             nodes = [n for n in nodes if n not in visited]
        
#         return ans

# #Time Limit Exceeded
#------------------------------------------------------------------
        
   