class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #minPath disjkra
        # make BFS with q

        n = len(grid)

        heap = [ (grid[n-1][n-1], n-1,n-1 )]
        visited = set( [(n-1, n-1)] )

        while heap:
            curr_time,i,j = heapq.heappop(heap)

            #print("1:", heap,visited,(i,j),curr_time)

            if (i,j) == (0,0):
                return curr_time

            for neig_i,neig_j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                #print("  2:", neig_i,neig_j, neig_i >= 0 and neig_i < n and neig_j >= 0 and neig_j > n and (neig_i,neig_j) not in visited)
                if neig_i >= 0 and neig_i < n and neig_j >= 0 and neig_j < n and (neig_i,neig_j) not in visited:
                        visited.add((neig_i,neig_j))
                        time = max(curr_time, grid[neig_i][neig_j])
                        heapq.heappush(heap,(time,neig_i,neig_j) )
        



