class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        
        #https://www.youtube.com/watch?v=0iKnobUck9c
        #disjkra & binary tree

        def check(limit):
            h = [(0,0)] #peso, nodo
            dist = [k+1]*n
            dist[0] = 0

            while h:
                w,node = heapq.heappop(h)

                if node == n-1:
                    return True

                if w > dist[node]:
                    continue

                for nw,neig in adj[node]:
                    if nw < limit:
                        continue

                    accum = w + nw
                    if accum < dist[neig]:
                        dist[neig]  = accum
                        heapq.heappush(h, (accum,neig))

            return False

        
        l = float("inf")
        r = 0 
        n = len(online)

        adj = defaultdict(list)
        for a,b,w in edges:
            if not online[a] or  not online[b]:
                continue
            adj[a].append((w,b))
            l = min(l,w)
            r = max(r,w)

        ans = -1
        while l<=r:
            mid = l + (r-l) // 2
            if check(mid):
                ans = mid
                l = mid+1
            else:
                r = mid -1



        return ans







