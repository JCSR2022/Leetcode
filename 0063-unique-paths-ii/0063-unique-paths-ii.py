class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        #aproach
        #create adhjacen list
        #dfs all paths from begin-end
        
        
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
        
#         if m == 1 and n==1:
#             if obstacleGrid[0][0] == 1:
#                 return 0
#             else:
#                 return 1
            
            
        
        
#         def pos_moves(i,j):
            
#             moves = []
#             #down
#             if i+1 < m and obstacleGrid[i+1][j] == 0:
#                 moves.append((i+1,j))
            
#             #right
#             if j+1 < n and obstacleGrid[i][j+1] == 0:
#                 moves.append((i,j+1))
            
#             return moves
        
#         def BFS_paths():
#             q = deque()
#             visited = set()
#             count_paths = 0
#             q.append((0,0))
            
#             while q:
#                 node = q.popleft()
                
#                 if node == (m-1,n-1):
#                     count_paths += 1
#                     continue
                        
#                 if node not in visited:
#                     visited.add(node)
                    
#                     for move in pos_moves(node[0],node[1]):
#                         q.append(move)
            
#             return count_paths  
        
#         return BFS_paths()

#Nooooooooooooooooooooooooooooooooooooo
#-------------------------------------------------------

#usign dp , 
    
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
            
        dp = {((m-1),(n-1)):1}
        
        def dfs(r,c):
            if r == m or c == n or obstacleGrid[r][c] == 1:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            
            return dp[(r,c)]
        
        
        return dfs(0,0)
        
                           
        
    
    
    
    
    
    
    
    
    
    
    
    
    
#------------------------------------------------------------------
    
#         m=len(obstacleGrid)
#         n=len(obstacleGrid[0])
#         res=[]
        
#         def backtrack(i,j):
#             if (i<m and i>=0 and j<n and j>=0) and obstacleGrid[i][j]!=1:
#                 if (i,j)==(m-1,n-1):
#                     #print(curr)
#                     #if curr not in res:  
#                     if obstacleGrid[i][j]==1:
#                         return 0
#                     mat[i][j]=1
#                 if mat[i][j]!=-1:
#                     return mat[i][j]                    
#                 mat[i][j]=backtrack(i+1,j)+backtrack(i,j+1)
                
#             else:
#                 mat[i][j]=0
#             return mat[i][j]
#         mat=[[-1]*(n+1) for elem in range(m+1)]
        
#         return backtrack(0,0)
                
                
                
                
            
            
        
        
        
        
        
        