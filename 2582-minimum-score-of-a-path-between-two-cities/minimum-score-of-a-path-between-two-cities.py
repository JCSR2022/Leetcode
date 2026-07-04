class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        # #dfs

        # adj = defaultdict(list)
        # for a,b,dist in roads:
        #     adj[a].append((b,dist))
        #     adj[b].append((a,dist))

        # for k,v in adj.items():
        #     print(k,v)
        
        # ans = float("inf")
        # visited = set()
        # visited.add(1)
        # queue = [(1,float("inf"))]
        # while queue:
        #     node,dist = queue.pop()
    
        #     ans = min(ans,dist)
        
        #     for neigh,dist in adj[node]:
        #         if neigh not in visited:
        #             visited.add(neigh)
        #             queue.append((neigh,dist))

        # return ans

#no imbecil
#----------------------------------------------------------



        adj = defaultdict(list)
        for a,b,dist in roads:
            adj[a].append((b,dist))
            adj[b].append((a,dist))

        ans = [float("inf")]*(n+1)
        visited = set()
        visited.add(1)
        queue = [(1,float("inf"))]
        while queue:
            node,dist = queue.pop()
    
            ans[node] = min(ans[node],dist)
        
            for neigh,new_dist in adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh,new_dist))
                else:
                    ans[neigh] = min(ans[neigh],new_dist)
            


        return min(ans)
