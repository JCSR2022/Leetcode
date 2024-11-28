class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
#         #dinamic program, go back count obstacles on each cell
        
#         m = len(grid)
#         n = len(grid[0])
        
#         obst_grid = [ [float("inf")]*n for _ in range(m)]
        
#         def pos_moves(i,j):
#             moves = []
#             if i < m-1:
#                 moves.append([i+1,j])
#             if i > 0:
#                 moves.append([i-1,j])
#             if j < n-1:
#                 moves.append([i,j+1])
#             if j > 0:
#                 moves.append([i,j-1])
#             return moves
        
        
#         def bfs():
#             heap = []
#             heappush(heap, (0,m+n,(m-1,n-1)))
            
#             while heap:
            
#                 obst_cont,dist,(x,y) = heappop(heap)
            
#                 if grid[x][y] == 1:
#                     obst_cont = obst_cont+1
#                 obst_grid[x][y] =  min(obst_grid[x][y],obst_cont)  
                
#                 if x == 0  and y == 0:
#                     return obst_cont
                
#                 # print(x,y, heap)
#                 # for row in obst_grid:
#                 #     print(row)
#                 # print()
                
#                 for i,j in pos_moves(x,y):
#                     new_dist = i+j
#                     if (new_dist,obst_cont, (i,j)) not in heap and obst_grid[i][j] > obst_cont:
#                             heappush(heap, (obst_cont,new_dist,(i,j)))
        
        
#         return bfs()
            
#----------------------------------------------------------------------------------


        queue = deque()
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        n = len(grid)
        m = len(grid[0])
        queue.append((0, 0, 0))
        visited.add((0, 0))
        while queue:
            i,j,count = queue.popleft()
            if i == n - 1 and j == m - 1:
                return count
            for x,y in dir:
                dx = x+i
                dy = y+j
                if dx>=0 and dx<n and dy>=0 and dy<m and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    if grid[dx][dy] == 1:
                        queue.append((dx, dy, count + 1))
                    else:
                        queue.appendleft((dx, dy, count))
        return -1
        