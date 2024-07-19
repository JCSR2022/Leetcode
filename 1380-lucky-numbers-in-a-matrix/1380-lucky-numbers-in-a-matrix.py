class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        
        #Brute stupid force
        
        
        ans = []
        
        for row in matrix:
            
            min_val = min(row)
            
            index_col = row.index(min_val)
            max_val = max([ r[index_col] for r in matrix ])
            
            if min_val == max_val:
                ans.append(min_val)
            
            
        
        return ans
        
        
        