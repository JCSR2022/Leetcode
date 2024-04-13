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
                        
        
        
        
#       #OPCION PROGRAMACION DINAMICA
    
#         m,n = len(matrix),len(matrix[0])
#         ans = 0
#         dp = {}

#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j]=='0':
#                     dp[(i,j)]=(0,0)
#                 else:
#                     x = dp[(i,j-1)][0]+1 if j>0 else 1
#                     y = dp[(i-1,j)][1]+1 if i>0 else 1
#                     dp[(i,j)] = (x,y)
#                     ans = max(x,y,ans)
#                     minWidth = x
#                     # verical max possible
#                     for r in range(i-1,i-y,-1):
#                         minWidth = min(minWidth,dp[(r,j)][0])
#                         ans = max(ans,minWidth*(i-r+1))


#         return ans

        

        
            if not matrix:
                return 0

            n = len(matrix[0])
            heights = [0] * (n + 1)
            max_area = 0

            for row in matrix:
                for i in range(n):
                    heights[i] = heights [i] + 1 if row[i] == '1' else 0

                stack = [-1]
                for i in range(n + 1):
                    while heights [i] < heights[stack[-1]]:
                        h = heights[stack.pop()]
                        w = i - stack[-1] - 1
                        max_area = max(max_area, h * w)

                    stack. append(i)

            return max_area

        
        