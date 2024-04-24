class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
#         hash_edges = {}

#         for e1, e2 in edges:
#             if e1 not in hash_edges:
#                 hash_edges[e1] = []
#             if e2 not in hash_edges:
#                 hash_edges[e2] = []
#             hash_edges[e1].append(e2)
#             hash_edges[e2].append(e1)

        
#         print(hash_edges)

        if n == 1:
            return [0] 

        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        print(adj)
        
        
        edge_cnt = {}
        leaves = deque()
        for src,neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_cnt[src] = len(neighbors)
            
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -=1
                for nei in adj[node]:
                    edge_cnt[nei] -=1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

    