class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x <= 1:
            return x
        
        # aproach: Binary search

        l = 0 
        r = x
        m = x
        cont = 0
        while cont < 1000:
            # breaks 100 iterations
            cont +=1

            m = (r+l)//2

            if m == l:
                return m      

            if m*m == x:
                return m

            elif m*m > x:
                r = m
            else:
                l = m

        return m
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if x==0 or x ==1:
#             return x
#         for i in range(x):
#             if i*i == x:
#                 return i
#             elif i*i > x:
#                 return i-1
        