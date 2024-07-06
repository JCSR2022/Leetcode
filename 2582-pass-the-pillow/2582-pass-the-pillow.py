class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        #@#%#^#^$W#%&$#&#$^@T
#         position  =  time%n
#         direction =  time//n
        
#         if direction%2 == 0 :
#             print(position ,direction)
            
#             return position+1
#         else:
#             print(position,n-position ,direction)
#             return n-(position+1)
        
        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))
        