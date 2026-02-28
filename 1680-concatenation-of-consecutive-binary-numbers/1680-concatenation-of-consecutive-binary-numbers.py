class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        #brute force
        mod = 10**9+7

        
        i=0
        ans=0
        for num in range(n,0,-1):
            for curr_bit in bin(num)[-1:1:-1]:
                if curr_bit == '1':
                    ans += 2**i
                    ans %= mod
                i +=1

        return ans
            