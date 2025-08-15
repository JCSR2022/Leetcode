class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1:
            return True
        
        if n < 4:
            return False

        bin_n = bin(n)[2:][::-1]
        return bin_n.count('1') == 1 and bin_n.index('1')%2 == 0
        