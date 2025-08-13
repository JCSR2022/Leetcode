class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 1:
            return True
            
        if abs(n) < 3:
            return False

        while abs(n) > 1:
            if n%3 != 0:
                return False
            n //=3
        
        return True
        