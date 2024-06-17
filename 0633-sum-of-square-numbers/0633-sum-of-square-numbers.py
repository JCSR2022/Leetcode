#import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        # brute force try all combinations
        
#         for i in range(c//2+2):
#             for j in range(i,c//2+2):
#                 #print(i,j,i**2+j**2,i**2+j**2==c)
#                 if i**2+j**2==c:
#                     return True
#         return False
        
        a = 0 
        while 2 * a * a <= c:
            b = (c - a * a) ** 0.5
            
            if int(b)**2 +a**2 == c:
                return True
            
            a +=1
            
        return False