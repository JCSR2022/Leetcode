class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
#         def suma_min(num,vector):
#             suma = [num+elem for elem in vector]
#             return  min(suma)
    
#         def vector_posibles(i,fila):
#             size = len(fila)
#             if i == 0:
#                 return fila[i:i+2]
#             elif 0 < i <size:
#                 return fila[i-1:i+2]
#             elif i == size:
#                 return fila[i-1:i+1]


#         size = len(matrix)  

#         # -100 <= matrix[i][j] <= 100
#         max_val = 101
#         matriz_minimos =  matrix.copy()  

#         for i in range(size-2,-1,-1):
#             for j in range(size):
#                 fila = matriz_minimos[i+1]
#                 vector = vector_posibles(j,fila)
#                 num = matrix[i][j]
#                 matriz_minimos[i][j] =suma_min(num,vector)
        
#         return min(matriz_minimos[0])
        
    
    
        n = len(matrix)
        dp = [ [0]*n for _ in range(n)]
        
        dp[0] = matrix[0]
        
        for i in range(1,n):
            for j in range(n):
                dp[i][j] = min( dp[i-1][max(0,j-1)] ,dp[i-1][j] ,dp[i-1][min(j+1,n-1)]) + matrix[i][j]
                
        print(dp)
        return min(dp[-1])
        
        
    
    
        