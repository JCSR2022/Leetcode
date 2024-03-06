class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    
        t = 0
        l = 0
        b = len(matrix) - 1
        r = len(matrix) - 1 
        
        while t<b:
            for i in range(b-t):
                temp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = temp
                
            t += 1
            b -= 1
            l += 1
            r -= 1
        
        return None
                
                
                 
            