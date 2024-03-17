class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowsCeros = []
        columnsCeros = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsCeros.append(i)
                    columnsCeros.append(j)
                    
        for i in rowsCeros:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in columnsCeros:
                matrix[i][j] = 0
                
        