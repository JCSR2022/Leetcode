class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # todavia no le llego ni en ped...
        # https://www.youtube.com/watch?v=dkPYrvq5EmY
        
        # parent_sum - closer_node + further_nodes
        
        graph = defaultdict(list)
            
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
                
        # print(graph)
        # print()
        
        
        
        closer_nodes_count = [0] * n
        ans = [0] * n
        seen = set()
        def dfs(cur):
            nonlocal closer_nodes_count, ans, seen
            closer_nodes = 1 
            
            for child in graph[cur]:
                if child not in seen:
                    seen.add(child)
                    child_nodes_count = dfs(child)
                    closer_nodes += child_nodes_count
                    ans[0] += child_nodes_count
                    
            closer_nodes_count[cur] = closer_nodes
            
            return closer_nodes
        
        seen.add(0)
        dfs(0)
                        
#         print(closer_nodes_count)
#         print()
#         print(ans)
         
        
        visited = set()
        def dfs2(cur):
            nonlocal ans
            for child in graph[cur]:
                if child not in visited:
                    visited.add(child)
                    ans[child] = ans[cur] - closer_nodes_count[child] + (n - closer_nodes_count[child])
                    dfs2(child)
        
        visited.add(0)
        dfs2(0)
        
        
     
        return ans
        
            