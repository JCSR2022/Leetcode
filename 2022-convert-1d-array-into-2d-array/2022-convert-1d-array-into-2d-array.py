class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        
        if len(original) != m*n:
            return []
        
        
        arr_2d = [ [0] *n for _ in range(m) ]

        
        for i,num in enumerate(original):
           
            arr_2d[i//n][i%n]=num        
            
            
        return arr_2d
    
    
    
    