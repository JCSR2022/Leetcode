class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        
        return bin(n).count('1') == 1 and bin(n).count('-') == 0
        
    
        