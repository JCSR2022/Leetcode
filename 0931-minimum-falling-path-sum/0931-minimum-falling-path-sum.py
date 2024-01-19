class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def suma_min(num,vector):
            suma = [num+elem for elem in vector]
            return  min(suma)
    
        def vector_posibles(i,fila):
            size = len(fila)
            if i == 0:
                return fila[i:i+2]
            elif 0 < i <size:
                return fila[i-1:i+2]
            elif i == size:
                return fila[i-1:i+1]


        size = len(matrix)  

        # -100 <= matrix[i][j] <= 100
        max_val = 101
        matriz_minimos =  matrix.copy()  

        for i in range(size-2,-1,-1):
            for j in range(size):
                fila = matriz_minimos[i+1]
                vector = vector_posibles(j,fila)
                num = matrix[i][j]
                matriz_minimos[i][j] =suma_min(num,vector)
        
        return min(matriz_minimos[0])
        
        