class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
  

        m, n = len(rowSum), len(colSum)
        res = [[0 for _ in range(n)] for _ in range(m)]
        i = j = 0
        while i < m and j < n:
            res[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]
            if not rowSum[i]: i += 1
            else: j += 1
        return res



#         rows = len(colSum)
#         cols = len(rowSum)
        
#         ans =  [[0] * cols for i in range(rows)]
        

        
        
#         return ans



    
#         rows = len(colSum)
#         cols = len(rowSum)
        
#         ans =  [[0] * cols for i in range(rows)]
        
#         for y in range(cols):
#             x = 0
#             while colSum[y] > 0:
#                 print(ans,x,y)
#                 ans[x][y] = min(colSum[y],rowSum[x])
#                 colSum[y] -= ans[x][y]
#                 rowSum[x] -= ans[x][y]
                
#                 x += 1
#         print(ans)
#         return ans    





    
        #         for i,row in enumerate(ans): row[0] =  rowSum[i]
            
        

        
#         def checkcolSum(matrix,colSum):
#             my_ColSum = [0] * len(matrix[0])
            
#             for row in matrix:
#                 for i,col_val in enumerate(row):
#                     my_ColSum[i] +=col_val
                
#             return my_ColSum == colSum
                    
#         print(ans)
#         print(checkcolSum(ans,colSum))
        
        
#         for row 
        
        
        
        
#         ans = [[3,0],[1,7]]
#         return ans
        

#         [3 0] .... [2 1]...
#         [8 0] .... [7 1].. []

#         [3 0] 
#         [1 7]
        
#         [2 1] 
#         [2 6]
        
#         [1 2]
#         [3 5]
       
#         [0 3]
#         [4 4]
        
        #what?????
        # F#$^#@$^#%&%
    
 #       a + b = r1
 #       c + d = r2
 #      -------
 #       c1  c2 
    
#      b = c2 - d
#      a = c1 - c

 #       c1 - c + c2 - d = r1
 #            c + d      = r2
