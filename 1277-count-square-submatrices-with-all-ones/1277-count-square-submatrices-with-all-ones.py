class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        

        #dfs , mark visited , expand as squares

        # def check_k(matrix, i, j):

        #     k = 1  # empezamos con tamaño 1x1
        #     while i + k < m and j + k < n:
        #         # revisar la nueva columna (a la derecha)
        #         for r in range(i, i + k + 1):
        #             if matrix[r][j + k] == 0:
        #                 return k
                
        #         # revisar la nueva fila (abajo)
        #         for c in range(j, j + k + 1):
        #             if matrix[i + k][c] == 0:
        #                 return k
                
        #         # si todo está bien, podemos expandir
        #         k += 1
        #     return k

        # def mark_visited(matrix_visited,i,j,k):
        #     for i_k in range(i,i+k):
        #         for i_j in range(j,j+k):
        #             matrix_visited[i_k][i_j] = True
    

        # def sum_of_squares(n: int) -> int:
        #     #return sum(i**2 for i in range(1, n+1))
        #     return n * (n + 1) * (2*n + 1) // 6

        # def printMatrix(matrix):
        #     for row in matrix:
        #         print(row)
        #     print()


        # m = len(matrix)
        # n = len(matrix[0])
        # ans = 0
        # visited = [[False]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] != 0 and not visited[i][j]:
        #             k = check_k(matrix,i,j)
        #             ans += sum_of_squares(k)
        #             mark_visited(visited,i,j,k)

        #             print("(i,j)",i,j,"k:",k,"ans:",ans)
        #             printMatrix(visited)

        # return ans

#no funciona porque la logica esta mal!!! 
#matrix = [[0,0,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1]]
#matrix = [[1,0,1,0,1],[1,0,0,1,1],[0,1,0,1,1],[1,0,0,1,1]]
#--------------------------------------------------------------------------

        def printMatrix(matrix):
            for row in matrix:
                print(row)
            print()

    #https://www.youtube.com/watch?v=5VSKOeSqk-M

    #using Dp
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                #print("(i,j)",i,j)
                if matrix[i][j] == 0:
                    continue
    
                if i-1 >= 0 and j-1 >= 0:
                    col = [matrix[x][j-1] for x in range(i-1,i+1)]
                    #print( "col:",col)
                    row = [matrix[i-1][y] for y in range(j-1,j+1)]
                    #print("row:",row  )
                    min_total = min(col+row)
                    matrix[i][j] +=min_total    

                #printMatrix(matrix)

        return sum(sum(matrix[i][j] for j in range(n)) for i in range(m))

                

                    



        