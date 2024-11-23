class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        
#         def rotar_matriz_90_clockwise(matriz):
#             """
#             Rota una matriz 90 grados en sentido horario.

#             :param matriz: Lista de listas que representa la matriz.
#             :return: La matriz rotada.
#             """
#             # Transponer la matriz
#             matriz_transpuesta = list(zip(*matriz))

#             # Invertir cada fila de la matriz transpuesta
#             matriz_rotada = [list(fila)[::-1] for fila in matriz_transpuesta]

#             return matriz_rotada
        
        
#         def gravedad(columna):
#             size = len(columna)
#             print(columna)
#             for i in range(size-1,-1,-1):
#                 print(i,columna[i])
                
        


#         matriz_rotada = rotar_matriz_90_clockwise(box)

#         print(matriz_rotada)
            
#         gravedad(matriz_rotada[0])
        
        
#         return matriz_rotada


#----------------------------------------------------------------------------

        m, n = len(box), len(box[0])
        
        # Process each row to simulate gravity
        for row in box:
            empty_slot = n - 1  # Start from the rightmost column
            
            for col in range(n - 1, -1, -1):  # Traverse the row from right to left
                if row[col] == '#':  # Stone
                    row[col], row[empty_slot] = row[empty_slot], row[col]
                    empty_slot -= 1
                elif row[col] == '*':  # Obstacle
                    empty_slot = col - 1
        
        # Rotate the box clockwise
        rotated_box = [[None] * m for _ in range(n)]  # Create a rotated matrix
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = box[i][j]
        
        return rotated_box


        