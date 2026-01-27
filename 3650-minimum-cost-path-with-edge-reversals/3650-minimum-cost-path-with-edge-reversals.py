class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:

        #Aproach create paths missing , use disjkra

        adj_list = defaultdict(list)
        for u,v,w in edges:
            adj_list[u].append((w,v))
            adj_list[v].append((2*w,u))

        heap = []
        heapq.heappush( heap, (0,0) )
        visited = set()
        min_weight = float("inf")

        while heap:
            weight,node = heapq.heappop(heap)

            if node == n-1:
                min_weight = min(min_weight,weight)
                continue
            
            if node not in visited:
                visited.add(node)

                for neigh_w,neigh_n in adj_list[node]:
                    if neigh_n not in visited:
                        heapq.heappush( heap, (neigh_w+weight,neigh_n) )

        return  min_weight if  min_weight < float("inf") else -1





        