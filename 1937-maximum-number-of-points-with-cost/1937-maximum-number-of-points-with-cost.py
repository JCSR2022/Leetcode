class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
#         #dinamic O( m * n^2)
        
#         rows = len(points)
#         columns = len(points[0])
        
#         if rows == 1:
#             return max(points[0])

#         dp_matrix = [ [0]*columns for _ in range(rows) ]
        
#         dp_matrix[0] =  points[0]
        
#         for i in range(1,rows):
#             for j in range(columns):
#                 dp_matrix[i][j] = max([dp_matrix[i-1][k] -abs(k-j) for k in range(columns)])  
                
#             for j in range(columns):
#                 dp_matrix[i][j] += points[i][j]
    
#         return max(dp_matrix[-1])
    
    
    
    
        #dinamic O( m * n) using memory
        
        rows = len(points)
        columns = len(points[0])
        
        if rows == 1:
            return max(points[0])

        dp_matrix = [ [0]*columns for _ in range(rows) ]
        dp_matrix[0] =  points[0]
        left = [0]*columns
        right = [0]*columns
        
        
        for i in range(1,rows):
            
            
            for j in range(columns):
                if j == 0:
                    left[j] = dp_matrix[i-1][j]
                else:
                    left[j] = max( left[j-1] -1 ,dp_matrix[i-1][j])  
            
            
            for j in range(columns-1,-1,-1):
                if j == columns-1:
                    right[j] = dp_matrix[i-1][j]
                else:
                    right[j] = max(right[j+1]-1, dp_matrix[i-1][j])
                    
            for j in range(columns):
                dp_matrix[i][j] = max(left[j],right[j]) + points[i][j]
    
        return max(dp_matrix[-1])
        
        