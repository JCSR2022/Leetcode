class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        # the most brute force of all: (n*m)**2
        
#         def check1(i,j,k,l):
#             ans = True
#             for n in range(i,k):
#                 for m in range(j,l):
#                     if matrix[n][m] == '0':
#                         return False
#             return ans

#         def sub_matrix(i,j,k,l):
#             subMatrix = []
#             for n in range(i,k):
#                 subMatrix.append([])
#                 for m in range(j,l):
#                     subMatrix[-1].append(matrix[n][m])
#             return subMatrix 


#         maxSize = 0    
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 for k in range(i+1,len(matrix)+1):
#                     for l in range(j+1,len(matrix[0])+1):
#                         if check1(i,j,k,l):
#                             maxSize = max(maxSize, (k-i)*(l-j))
#                             #print(i,j,sub_matrix(i,j,k,l), (k-i)*(l-j))
#         return maxSize
                        
        
        
        
        
        #que es un rectangulo?
        # es un conjunto de filas que se repite por columnas
        #  un rectangulo de tamaño  (i_down-i_up) * ( j_right - j_left )
        # for j in range(j_left, j_right)
        #   for i in range(i_up,i_down):
        #      all matrix[i][j] =1 
        #
        
    
        m,n = len(matrix),len(matrix[0])
        ans = 0
        dp = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':
                    dp[(i,j)]=(0,0)
                else:
                    x = dp[(i,j-1)][0]+1 if j>0 else 1
                    y = dp[(i-1,j)][1]+1 if i>0 else 1
                    dp[(i,j)] = (x,y)
                    ans = max(x,y,ans)
                    minWidth = x
                    # verical max possible
                    for r in range(i-1,i-y,-1):
                        minWidth = min(minWidth,dp[(r,j)][0])
                        ans = max(ans,minWidth*(i-r+1))


        return ans

        
        
        