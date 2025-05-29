class Solution:


    def dfs(self, node: int, color: int, graph: List[List[int]],
            component: List[int], bipartite: List[int]) -> None:
        bipartite[color] += 1
        component[node] = color
        for neighbor in graph[node]:
            if component[neighbor] == -1:
                self.dfs(neighbor, 1 - color, graph, component, bipartite)

    def build_graph(self, edges: List[List[int]], n: int) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph


    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:


        n1, n2 = len(edges1) + 1, len(edges2) + 1


        graph1 = self.build_graph(edges1, n1)
        graph2 = self.build_graph(edges2, n2)

 
        component1 = [-1] * n1
        bipartite1 = [0, 0]
        self.dfs(0, 0, graph1, component1, bipartite1)


        ans = [bipartite1[component1[i]] for i in range(n1)]


        component2 = [-1] * n2
        bipartite2 = [0, 0]
        self.dfs(0, 0, graph2, component2, bipartite2)

        max_bipartite2 = max(bipartite2)
        return [val + max_bipartite2 for val in ans]




#vete a la maldita mierda
        #aproach
        #find for edges 1 ,for each node max even targets
        #find for edges 2 ,max odd targets

        # n = len(edges1)+1
        # m = len(edges2)+1

        # #trees:
        # tree1 = defaultdict(list)
        # for ai,bi in edges1:
        #     tree1[ai].append(bi)
        #     tree1[bi].append(ai)

        # tree2 = defaultdict(list)
        # for ui,vi in edges2:
        #     tree2[ui].append(vi)
        #     tree2[vi].append(ui)

        # print(dict(tree1))
        # print(dict(tree2))


        # def dfs_tree1(node,edges,prev_node =-1):
            
        #     if len(tree1[node]) == 1:
        #         if edges%2 == 0 :
        #             return 1
        #         else:
        #             return 0

        #     count_nodes = 0
        #     for neighbor in tree1[node]:
        #         if neighbor != prev_node:
        #             count_nodes +=  dfs_tree1(neighbor,edges+1,node)
                
        #     if count_nodes != 0:
        #         return count_nodes + 1
        #     else:
        #         return 0


        # ans = [0]*n
        # for i in range(n):
        #     ans[i] = dfs_tree1(i,0) 

        # print(ans)



        # def bfs_tree1(curr_root):
            
        #     q = deque()
        #     q.append((curr_root,0,-1))

        #     while q:
        #         node,edges_cnt,prev_node = q.popleft()

        #         if edges_cnt%2 == 0:
        #             ????????

        #         for 







































        # def dfs_odds_tree1(node,count_edges,prev = -1):

        #     print(node,tree1[node],count_edges)

        #     if len(tree1[node]) == 1:
        #         if count_edges%2 == 0:
        #             return 1
        #         else:
        #             return 0

        #     curr_count = 0
        #     for neigh in tree1[node]:
        #         if neigh != prev:
        #             curr_count += dfs_odds_tree1(neigh,count_edges+1,node)

        #     print("curr_count: ",curr_count)

        #     if curr_count == 0:
        #         return 0
        #     else:
        #         return curr_count+1


        # arr1 = []
        # for i in range(n):
        #     arr1.append(dfs_odds_tree1(i,0))
        #     print("---------")

        # print()
        # print(arr1)
        # print()

        # def dfs_odds(node,tree,count_edges,prev=-1):

        #     print(node,tree[node],count_edges)

        #     if len(tree[node]) == 1 and count_edges%2 == 0:
        #         return 1
        #     else:
        #         return 0 

        #     curr_cnt = 0
        #     for neigh in tree[node]:
        #         if neigh != prev:
        #             curr_cnt += dfs_odds(neigh,tree,count_edges+1,node)
            
        #     if curr_cnt > 0:
        #         return curr_cnt + 1
        #     else:
        #         return 0 

        # arr1 = []
        # for i in range(n):
        #     arr1.append(dfs_odds(i,tree1,0))
        # print(arr1)

        # arr2 = []
        # for i in range(m):
        #     arr2.append(dfs_odds(i,tree2,0))

        
        # print(arr2)        




        ans = [1]*n
        return ans
        