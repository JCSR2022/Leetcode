class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
#         new_grid = [ [0]*len(grid[0]) for _ in range(len(grid))]
        
#         def expandOnes(i,j,radio = 0):
#             print(i,j,radio,min(i,j) < 0 or i > len(grid)-1 or j >len(grid)-1)
#             if min(i,j) < 0 or i > len(grid)-1 or j >len(grid)-1:
#                 return
            
#             adj = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            
            
#             if radio == 0:
#                 new_grid[i][j] = 0
#                 for x,y in adj:
#                     expandOnes(x,y,radio+1)
            
#             if new_grid[i][j] == 0 :
#                 new_grid[i][j] = radio
#                 return 
                
#             if new_grid[i][j] > radio:
#                 new_grid[i][j] = radio
#                 return
            
                
                
#         for i in range(len(grid)):
#             for j in range(len(grid)):
#                 if grid[i][j] == 1:
#                     expandOnes(i,j)
        
#         print()
#         for row in new_grid:
#             print(row)
        

#         return 0
#     no pude ni hacer esta mierda

# Find the Safest Path in a Grid - Leetcode 2812 - Python
# https://www.youtube.com/watch?v=-5mQcNiVWTs






        N = len(grid)
    
    
        def in_bounds(r,c):
            return min(r,c) >=0 and max(r,c) < N
    
        def precompute():
            q = deque()
            min_dist = {}
            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append([r,c,0])
                        min_dist[(r,c)]= 0 
            while q:
                r,c,dist = q.popleft()
                nei = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                
                for r2,c2 in nei:
                    if in_bounds(r2,c2) and (r2,c2) not in min_dist:
                        min_dist[(r2,c2)] = dist+1
                        q.append([r2,c2,dist+1])
                        
            return min_dist
        
        
        min_dist = precompute()
        
        
#         new_grid = [ [0]*len(grid[0]) for _ in range(len(grid))]
#         for key,val in  min_dist.items():
#                 new_grid[key[0]][key[1]] = val
#         for row in new_grid:
#             print(row)
            
        maxHeap = [(-min_dist[(0,0)], 0, 0)] # (dist,r,c)
        visit = set()
        visit.add((0,0))
        
        while maxHeap:
            dist,r,c = heapq.heappop(maxHeap)
            dist = -dist
            
            if (r,c) == (N-1,N-1):
                return dist
            
            nei = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            
            for r2, c2 in nei:
                if in_bounds(r2,c2) and (r2,c2) not in visit:
                    visit.add((r2,c2))
                    dist2 = min(dist,min_dist[(r2,c2)])
                    heapq.heappush(maxHeap,(-dist2,r2,c2))
                    
            
            
 
                
                        
            
            
            