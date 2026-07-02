class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        #aproach disjkra?

        m = len(grid)
        n = len(grid[0])

        heap = []
        heapq.heappush(heap,(grid[0][0],0,0)) # (damage,i,j)
        visited = set()
        visited.add((0,0))
        while heap:
            damage,i,j = heapq.heappop(heap)

            
            if damage == health:
                return False

            if (i,j) == (m-1,n-1):
                return True

            

            for mov_i,mov_j in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_i = i+mov_i
                new_j = j+mov_j
                if  new_i>=0 and new_i<m and new_j>=0 and new_j<n and (new_i,new_j) not in visited:
                    visited.add((new_i,new_j ))
                    heapq.heappush(heap,(damage+grid[new_i][new_j],new_i,new_j))
                    
        
        return False



