class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        #brute force build matrix, for each guard modify matrix count values 0 
        
        #matrix = [[ 0 if [i, j] not in guards and [i, j] not in walls else -1 for j in range(n)]
        #            for i in range(m) ]
        
        matrix = [ [0]*n for _ in range(m)]
        for i,j in guards:
            matrix[i][j] = -1
        for i,j in walls:
            matrix[i][j] = -1
        
        def fill_view(i,j):
            #north
            for k in range(i-1,-1,-1):
                if matrix[k][j] >= 0:
                    matrix[k][j] = 1
                else:
                    break
        
            #south
            for k in range(i+1,m):
                if matrix[k][j] >= 0:
                    matrix[k][j] = 1
                else:
                    break
                    
            #east
            for k in range(j-1,-1,-1):
                if matrix[i][k] >= 0:
                    matrix[i][k] = 1
                else:
                    break
            
            #west
            for k in range(j+1,n):
                if matrix[i][k] >= 0:
                    matrix[i][k] = 1
                else:
                    break
        
        # def print_matrix():
        #     for row in matrix:
        #         print(row)
        #     print()
        
        for i,j in guards:
            fill_view(i,j)
            # print(i,j)
            # print_matrix()
        
        
        
        ans = sum([row.count(0) for row in matrix])


        return ans
        
        
  #---------------------------------------------------------


#         matrix = [[ 0 if [i, j] not in guards and [i, j] not in walls else -1 for j in range(n)]
#                     for i in range(m) ]
        
#         def fill_view(i,j):
#             #north
#             k = i-1
#             while k >= 0:
#                 if matrix[k][j] >= 0:
#                     matrix[k][j] = 1
#                     k -= 1
#                 else:
#                     break
            
#             #south
#             k = i+1
#             while k < m:
#                 if matrix[k][j] >= 0:
#                     matrix[k][j] = 1
#                     k += 1
#                 else:
#                     break
                    
#             #east
#             k = j-1
#             while k >= 0:
#                 if matrix[i][k] >= 0:
#                     matrix[i][k] = 1
#                     k -= 1
#                 else:
#                     break
            
#             #west
#             k = j+1
#             while k < n:
#                 if matrix[i][k] >= 0:
#                     matrix[i][k] = 1
#                     k += 1
#                 else:
#                     break
                        
#         for i,j in guards:
#             fill_view(i,j)
            
#         ans = sum([row.count(0) for row in matrix])


#         return ans
        
        
        