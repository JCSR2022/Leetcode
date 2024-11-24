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


#         def gravety_leftside(row):
#             i = n - 1
#             for c in range(n-1,-1,-1):
#                 if box[row][c] == "#":
#                     box[row][c] = box[row][i]
#                     box[row][i] = "#"
#                     i += 1
#                 elif box[row][c] == "*":
#                     i += c+1    
        
#         m = len(box)
#         n = len(box[0])

#         gravety_leftside(0)
        
#         return box
                

#-------------------------------------------------------------

#         rows, cols = len(box),len(box[0])
    
#         # gravety_leftside
#         for r in range(rows):
#             i = cols -1
#             for c in reversed(range(cols)):
#                 if box[r][c] == "#":
#                     box[r][c],box[r][i] = box[r][i],box[r][c]
#                     i -= 1
#                 elif box[r][c] == "*":
#                     i = c - 1

#         matriz_transpuesta = list(zip(*box)) 
#         return [list(fila)[::-1] for fila in matriz_transpuesta]
                    
            
#-------------------------------------------------------------   

        cols = len(box[0])
    
        # gravety_leftside
        for r in range(len(box)):
            i = cols -1
            for c in reversed(range(cols)):
                if box[r][c] == "#":
                    box[r][c],box[r][i] = box[r][i],box[r][c]
                    i -= 1
                elif box[r][c] == "*":
                    i = c - 1

        return [list(fila)[::-1] for fila in list(zip(*box)) ]                


        