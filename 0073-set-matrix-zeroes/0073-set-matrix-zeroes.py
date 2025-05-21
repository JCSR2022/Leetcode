class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # #sol O(n)
        # m = len(matrix)
        # n = len(matrix[0])

        # rows = set()
        # col = set()        
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             if i not in rows:
        #                 rows.add(i)
        #                 for y in range(n):
        #                     matrix[i][y] = 0
        #             if j not in col:    
        #                 col.add(j)
        #                 for x in range(m):
        #                     matrix[x][j] = 0
#nooooo
#----------------------------------------------------
        

        #sol O(n)
        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        col = set()        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)    
                    col.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in col:
                    matrix[i][j] = 0
     





































        # rowsCeros = []
        # columnsCeros = []
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             rowsCeros.append(i)
        #             columnsCeros.append(j)
                    
        # for i in rowsCeros:
        #     for j in range(len(matrix[0])):
        #         matrix[i][j] = 0
        
        # for i in range(len(matrix)):
        #     for j in columnsCeros:
        #         matrix[i][j] = 0
                
        