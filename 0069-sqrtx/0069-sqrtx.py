class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0
        r =x
        ans = 0
        
        while l <=r:
            m = l + ((r-l)//2)
            
            if m*m > x:
                r = m -1
            elif m*m < x:
                l = m + 1
                ans = m
            else:
                return m
        
        return ans
            
             
   













#         if x <= 1:
#             return x
        
#         # aproach: Binary search

#         l = 0 
#         r = x
#         m = x
#         cont = 0
#         while cont < 1000:
#             # breaks 100 iterations
#             cont +=1

#             m = (r+l)//2

#             if m == l:
#                 return m      

#             if m*m == x:
#                 return m

#             elif m*m > x:
#                 r = m
#             else:
#                 l = m

#         return m
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if x==0 or x ==1:
#             return x
#         for i in range(x):
#             if i*i == x:
#                 return i
#             elif i*i > x:
#                 return i-1
        