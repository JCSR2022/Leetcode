class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        #brut force, try al combinations of columns flips O(n^2*m)
        # no O(2^n*m*n)
        
        #------------------------------------------------------
        
        #count equivalents rows:
        
        for i in range(len(matrix)):
            matrix[i] = tuple(matrix[i])
            
        
        def inv_row(arr):
            return tuple([0 if i == 1 else 1 for i in arr])
        
        equ_rows = {}
        
        for row in matrix:
            #print(row,inv_row(row),equ_rows)
            if row in equ_rows:
                equ_rows[row] += 1
                continue
            row_inv = inv_row(row)
            if row_inv in equ_rows:
                equ_rows[row_inv] += 1
                continue
            equ_rows[row] = 1
        
        #print(equ_rows)
        return max(equ_rows.values() )
        
        
            
        
        